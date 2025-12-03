# Unused. Level 2 works for two exercises
def get_largest_joltage_level_1(battery):
    battery_list = list(battery)
    first_max = max(battery_list[:-1])
    index_first_max = battery_list.index(first_max)
    second_max = max(battery_list[index_first_max+1:])

    return int(first_max + second_max)

def get_largest_joltage_level_2(battery, num_batteries):
    battery_list = list(battery)
    maxes = []
    indexes = []

    for i in range(0, num_batteries):
        start_partial = indexes[i - 1] + 1 if len(indexes) != 0 else 0
        end_partial = len(battery_list) +1 - num_batteries + i
        partial_list = battery_list[start_partial:end_partial]
        maxes.append(max(partial_list))
        indexes.append(partial_list.index(maxes[i]) + start_partial)

    return int(''.join(maxes))

class Day03:

    def __init__(self):
        self.batteries = []
        self.joltage = 0

    def load_batteries(self):
        with open("input.dat", "r") as file:
            self.batteries = file.read().splitlines()

    def load_alt_batteries(self):
        with open("test.dat", "r") as file:
            self.batteries = file.read().splitlines()

    def print_battery_list(self):
        for bat in self.batteries:
            print(bat)

    def get_largest_joltage_level_1(self):
        for bat in self.batteries:
            self.joltage += get_largest_joltage_level_2(bat, 2)
        print(f"Total output joltage is: {self.joltage}")

    def get_largest_joltage_level_2(self):
        for bat in self.batteries:
            self.joltage += get_largest_joltage_level_2(bat, 12)
        print(f"Total output joltage is: {self.joltage}")

day03 = Day03()
day03.load_batteries()
day03.print_battery_list()
#day03.get_largest_joltage_level_1()
day03.get_largest_joltage_level_2()
