import math

RIGHT = "R"
LEFT = "L"
MAX_VALUE = 100

class Spinner:

    def __init__(self, initial):
        self.input_data = []
        self.position = initial
    #    print(f"The dial starts by pointing at {self.position}.")
        self.clicks = 0

    def load_list(self):
        with open("input.dat", "r") as f:
            self.input_data = f.read().splitlines()

    def load_test_list(self):
        with open("test.dat", "r") as f:
            self.input_data = f.read().splitlines()

    def print_list(self):
        print(self.input_data)

    def rotate_list(self):
        for i in self.input_data:
            self.rotate_value((i[0], int(i[1:])))
        print(f"Lock has landed at zero {self.clicks} times.")

    def rotate_value(self, value):
        if value[0] == RIGHT:
            end = self.position + value[1]
            finalPosition = end % MAX_VALUE
        else:
            end = self.position - value[1]
            finalPosition = end % MAX_VALUE

        zeros = 0

        if end <= 0:
            zeros = (abs(end) + MAX_VALUE) // MAX_VALUE

        if end >= MAX_VALUE:
            zeros = end // MAX_VALUE

        if self.position == 0 and zeros > 0 and end <= 0:
            zeros -= 1

        # print(f"The dial is rotated {value[0]}{value[1]} to point at {finalPosition}; during this rotation, it points at zero {zeros} times")

        self.position = finalPosition
        self.clicks += zeros

spinner = Spinner(initial=50)

spinner.load_list()
spinner.rotate_list()
