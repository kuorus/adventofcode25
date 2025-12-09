TEST = "test.dat"
REAL = "input.dat"

class Point:
    def __init__(self, x: int, y: int, points: int):
        self.x = x
        self.y = y
        self.areas = [0] * points 

    def calculate_area(self, b_point: Point, id: int):
        x_len = abs(self.x - b_point.x) + 1
        y_len = abs(self.y - b_point.y) + 1 
        self.areas[id] = x_len * y_len

class Day09:

    coordinates: list[Point]
    largest: int
    
    def __init__(self, environment: str):
        self.coordinates = []
        self.largest = 0
        self.environment = environment

    def load_coordinates(self):
        with open(self.environment) as f:
            content = f.read().splitlines()
            for line in content:
                x, y = line.split(",")
                self.coordinates.append(Point(int(x), int(y), len(content)))
    
    def calculate_areas(self):
        for i in range(len(self.coordinates)):
            for j in range(len(self.coordinates)):
                if i != j:
                    self.coordinates[i].calculate_area(self.coordinates[j], j)

    def get_largest_area(self):
        largests = list(map(lambda x: max(x.areas), self.coordinates))
        self.largest = max(largests)
        print(f"Largest area size is: {self.largest} sq. units")

day09 = Day09(REAL)
day09.load_coordinates()
day09.calculate_areas()
day09.get_largest_area()

