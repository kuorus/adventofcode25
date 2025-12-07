START = 'S'
SPLITTER = '^'
BEAM = '|'

from functools import reduce

class Day07:
    def __init__(self):
        self.map = []
        self.splits = 0
        self.timelines = 0
    
    def load_map(self, filename):
        with open(filename) as f:
            self.map = f.read().splitlines()

    def load_map_level_2(self, filename):
        with open(filename) as f:
            self.map = f.read().splitlines()
            self.map = list(map(lambda x: x.replace(".", "0"), self.map))
            self.map = list(map(lambda x: list(x), self.map))
            for i in range(len(self.map)):
                for j in range(len(self.map[i])):
                    self.map[i][j] = 0 if self.map[i][j] == "0" else self.map[i][j]

    def print_map(self):
        print("Map:")
        for line in self.map:
            for item in line:
                print(item if item != 0 else " ", end="\t")
            print()
            

    def print_splits(self):
        print(f"Total beam splits: {self.splits}")

    def move_across_map(self):
        beam_indexes = set()
        for row_index in range(len(self.map[:-1])):
            line = self.map[row_index]
            if START in line:
                start_index = line.index(START)
                row = self.map[row_index+1]
                self.map[row_index+1] = row[0:start_index] + BEAM + row[start_index+1:]
                beam_indexes.add(start_index)
            else:
                new_beam_indexes = set()
                for beam_index in beam_indexes:
                    row = self.map[row_index+1]
                    if SPLITTER in row[beam_index]:
                        self.splits += 1
                        self.map[row_index+1] = row[0:beam_index-1] + BEAM + SPLITTER + BEAM + row[beam_index+2:]
                        new_beam_indexes.add(beam_index-1)
                        new_beam_indexes.add(beam_index+1)
                    else:
                        self.map[row_index+1] = row[0:beam_index] + BEAM + row[beam_index+1:]
                        new_beam_indexes.add(beam_index)
                beam_indexes = new_beam_indexes.copy()
    
    def move_level_2(self):
        beam_indexes = set()
        for row_index in range(len(self.map[:-1])):
            line = self.map[row_index]
            if START in line:
                start_index = line.index(START)
                row = self.map[row_index+1]
                self.map[row_index+1] = row[0:start_index] + [1] + row[start_index+1:]
                beam_indexes.add(start_index)
            else:
                new_beam_indexes = set()
                for beam_index in beam_indexes:
                    row = self.map[row_index+1]
                    if SPLITTER == row[beam_index]:
                        self.map[row_index+1] = row[:beam_index-1] + [self.map[row_index][beam_index] + row[beam_index-1] , SPLITTER, self.map[row_index][beam_index] + row[beam_index+1]] + row[beam_index+2:]
                        new_beam_indexes.add(beam_index-1)
                        new_beam_indexes.add(beam_index+1)
                    else:
                        self.map[row_index+1] = row[0:beam_index] + [self.map[row_index][beam_index] + row[beam_index]] + row[beam_index+1:]
                        new_beam_indexes.add(beam_index)
                beam_indexes = new_beam_indexes.copy()
        
    def print_timelines(self):
        self.timelines = reduce(lambda acc, curr: acc + curr, self.map[-1])
        print(f"Different timelines: {self.timelines}")

day07 = Day07()
day07.load_map_level_2("input.dat")
#day07.print_map()
day07.move_level_2()
#day07.move_across_map()
#day07.print_map()
#day07.print_splits()
day07.print_timelines()