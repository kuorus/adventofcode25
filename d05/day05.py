class Day05:
    def __init__(self):
        self.fresh_ingredients = []
        self.fresh_ranges = []
        self.stored_ingredients = []
    
    def process_storage(self):
        for ingredient in self.stored_ingredients:
            passed = False
            for fresh_range in self.fresh_ranges:
                if not passed and ingredient in range(fresh_range[0], fresh_range[1]+1):
                    self.fresh_ingredients.append(ingredient)
                    passed = True
        print(f"{len(self.fresh_ingredients)} are fresh in storage.")

    def process_file(self, file):
        for line in file:
            if "-" in line:
                line_range = line.split("-")
                self.fresh_ranges.append((int(line_range[0]), int(line_range[1])))
            else:
                if line != "":
                    self.stored_ingredients.append(int(line))

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
        print(self.stored_ingredients)

day05 = Day05()
day05.load_file()
day05.process_storage()