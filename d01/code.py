class Spinner:

    def __init__(self, initial):
        self.input_data = []
        self.position = initial
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
        if value[0] == "R":
            self.position += value[1]
        else:
            self.position -= value[1] 

        self.position %= 100

        if self.position == 0:
            self.clicks += 1

spinner = Spinner(initial=50)

spinner.load_list()
spinner.rotate_list()
