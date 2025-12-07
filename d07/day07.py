START = 'S'
SPLITTER = '^'
BEAM = '|'

class Day07:
    def __init__(self):
        self.map = []
        self.splits = 0
    
    def load_map(self, filename):
        with open(filename) as f:
            self.map = f.read().splitlines()

    def print_map(self):
        print("Map:")
        for line in self.map:
            print(line)

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
    
day07 = Day07()
day07.load_map("test.dat")
day07.print_map()
day07.move_across_map()
day07.print_map()
day07.print_splits()