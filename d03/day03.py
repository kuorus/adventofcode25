def get_largest_joltage(battery):
    battery_list = list(battery)
    first_max = max(battery_list[:-1])
    index_first_max = battery_list.index(first_max)
    second_max = max(battery_list[index_first_max+1:])
    return int(first_max + second_max)

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

    def get_largest_joltage(self):
        for bat in self.batteries:
            self.joltage += get_largest_joltage(bat)
        print(f"Total output joltage is: {self.joltage}")

day03 = Day03()
day03.load_batteries()
day03.print_battery_list()
day03.get_largest_joltage()