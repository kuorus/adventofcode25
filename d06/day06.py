import re
from functools import reduce

def evaluate(operator, a, b):
    if operator == '+': return a + b
    elif operator == '*': return a * b
    return 0

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

class Day06:
    def __init__(self):
        self.operands = []
        self.operators = []
        self.total = 0
    
    def load_file_level_1(self, filename):
        with open(filename) as f:
            lines = f.read().splitlines()
            for (index, line) in enumerate(lines):
                clean_line = re.sub("\\s+", " ", line.strip()).split(" ")
                if index != len(lines)-1:
                    self.operands.append(clean_line)
                else:
                    self.operators = clean_line
            self.operands = transpose_matrix(self.operands)
    
    def load_file_level_2(self, filename):
        with open(filename) as f:
            lines = f.read().splitlines()
            lines = transpose_matrix(lines)

            stack = []

            for line in lines:
                is_blank = "".join(line).isspace()            

                if line[-1] in ["+", "*"]:
                    self.operators.append(line[-1])
                
                joined = "".join(line[:-1])

                if not is_blank:
                    stack.append(int(joined))
                else:
                    self.operands.append(stack)
                    stack = []

            self.operands.append(stack)

    def calculate(self):
        for (index, calculation) in enumerate(self.operands):
            self.total += reduce(lambda acc, curr: evaluate(self.operators[index], acc, int(curr)), calculation[1:], int(calculation[0]))        

    def print_total(self):
        print(f"Total is: {self.total}")

day06 = Day06()
day06.load_file_level_1("input.dat")
day06.calculate()
day06.print_total()