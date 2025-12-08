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
    
    def print_nodes(self):
        for (i, node) in enumerate(self.nodes):
            print(i, end=": ")
            node.print()
    
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
        shortest = day08.get_shortest_link()
        return shortest["distance"] == math.inf

    def connect_circuits(self):
        for _ in range(10 if self.environment == TEST else 1000):
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

day08 = Day08(REAL)
day08.load_list()
day08.calculate_distances()
day08.connect_circuits()

sorted_list = sorted(day08.circuits, key=len, reverse=True)
print(f"Solution: {reduce(lambda acc, curr: acc * len(curr), sorted_list[:3], 1)}")