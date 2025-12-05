class Day05:
    def __init__(self):
        self.fresh_ingredients = 0
        self.fresh_ranges = []
    
    def process_storage(self):
        for (i, first) in enumerate(self.fresh_ranges):
            for j in range(i + 1, len(self.fresh_ranges)):
                if (i == len(self.fresh_ranges) - 1):
                    continue

                a, b = first[0], first[1]
                c, d = self.fresh_ranges[j][0], self.fresh_ranges[j][1]

                overlap = (a <= d) and (c <= b)

                if not overlap:
                    continue

                overlap_start = max(a, c)
                overlap_end = min(b, d)

                if overlap_start > c:
                    self.fresh_ranges.append((c, overlap_start - 1))

                if overlap_end < d:
                    self.fresh_ranges.append((overlap_end + 1, d))

                self.fresh_ranges[j] = (0,0) # delete but keep the position in list
               
        for fresh_range in self.fresh_ranges:
            if fresh_range[0] != 0:
                self.fresh_ingredients += (fresh_range[1] - fresh_range[0] + 1)
        
        print(f"{self.fresh_ingredients} fresh ingredient IDs")

    def process_file(self, file):
        for line in file:
            if "-" in line:
                line_range = line.split("-")
                self.fresh_ranges.append((int(line_range[0]), int(line_range[1])))
        self.fresh_ranges.sort()

    def load_test_file(self):
        with open("test.dat", "r") as f:
            file = f.read().splitlines()
            self.process_file(file)

    def load_file(self):
        with open("input.dat", "r") as f:
            file = f.read().splitlines()
            self.process_file(file)

    def print_fresh_ids(self):
        print(self.fresh_ranges)

day05 = Day05()
day05.load_file()
day05.process_storage()