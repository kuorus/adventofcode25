import math
from functools import reduce

TEST = "test.dat"
REAL = "input.dat"

class Node:
    def __init__(self, x, y, z, len_nodes):
        self.x = x
        self.y = y
        self.z = z
        self.distances = [math.inf] * len_nodes

    def distance_to_node(self, node, id):
        self.distances[id] = math.sqrt((node.x - self.x)**2 + (node.y - self.y)**2 + (node.z - self.z)**2)
    
    def get_shortest_distance(self):
        min_distance = min(self.distances)
        return min_distance, self.distances.index(min_distance)
    
class Day08:
    def __init__(self, environment=TEST):
        self.nodes = []
        self.circuits = []
        self.environment = environment
    
    def load_list(self):
        with open(self.environment) as f:
            lines = f.read().splitlines()
            for line in lines:
                x, y, z = line.split(",")
                self.nodes.append(Node(int(x), int(y), int(z), len(lines)))
    
    def calculate_distances(self):
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                if i != j:
                    self.nodes[i].distance_to_node(self.nodes[j], j)

    def get_shortest_link(self):
        distances = []
        for (index, node) in enumerate(self.nodes):
            distance, end = node.get_shortest_distance()
            distances.append({"origin": index, "end": end, "distance": distance})
        shortest = min(distances, key=lambda x: x.get("distance"))
        return shortest

    def all_nodes_connected(self):
        return len(self.circuits) == 1 and (len(self.circuits) > 0 and len(self.circuits[0]) == len(self.nodes))

    def connect_circuits_level_1(self):
        for _ in range(10 if self.environment == TEST else 1000):
            self.connect_circuits()
        sorted_list = sorted(day08.circuits, key=len, reverse=True)
        print(f"Solution for level 1: {reduce(lambda acc, curr: acc * len(curr), sorted_list[:3], 1)}")

    def connect_circuits_level_2(self):
        shortest = []
        while not self.all_nodes_connected():
            shortest = self.connect_circuits()
        print(f"Solution for level 2: {self.nodes[shortest["origin"]].x * self.nodes[shortest["end"]].x}")

    def connect_circuits(self):
        shortest = self.get_shortest_link()

        self.nodes[shortest["origin"]].distances[shortest["end"]] = math.inf
        self.nodes[shortest["end"]].distances[shortest["origin"]] = math.inf

        already_connected = []
        for circuit in self.circuits:
            if shortest["origin"] in circuit:
                already_connected.append(circuit)
                circuit.add(shortest["end"])
            elif shortest["end"] in circuit:
                already_connected.append(circuit)
                circuit.add(shortest["origin"])
        if len(already_connected) == 0:
            self.circuits.append(set([shortest["origin"], shortest["end"]]))
        elif len(already_connected) == 2:
            merged = already_connected[0].union(already_connected[1])
            self.circuits.append(merged)
            self.circuits.remove(already_connected[0])
            self.circuits.remove(already_connected[1])
        return shortest

day08 = Day08(REAL)
day08.load_list()
day08.calculate_distances()
day08.connect_circuits_level_1()
day08.connect_circuits_level_2()


