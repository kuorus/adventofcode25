EMPTY = "."
ROLL = "@"
REACHABLE = "x"

def is_left(col):
    return col == 0 

def is_right(col, size):
    return (col+1) == size

def is_top(row):
    return row == 0

def is_bottom(row, size):
    return (row+1) == size

def print_map(map):
    for line in map:
        print(line)

class Day04:
    def __init__(self):
        self.map = []
        self.adjacent_threshold = 4
        self.map_size_x = 0
        self.map_size_y = 0
        self.reachable_rolls = 0
    
    def load_test_map(self):
        with open('test.dat') as f:
            self.map = f.read().splitlines()

    def load_map(self):
        with open('input.dat') as f:
            self.map = f.read().splitlines()

    def print_map(self):
        print_map(self.map)

    def check_map(self):
        new_map = []

        self.map_size_x = len(self.map[0])
        self.map_size_y = len(self.map)

        for row in range(0, self.map_size_y):
            new_row = ""
            for col in range(0, self.map_size_x):
                if self.map[row][col] == EMPTY:
                    new_row += EMPTY
                else:
                    new_row += self.check_reachable_rolls(row, col)
            new_map.append(new_row)
        
        return new_map 

    def check_map_level_2(self):
        new_map = []

        self.map_size_x = len(self.map[0])
        self.map_size_y = len(self.map)

        for row in range(self.map_size_y):
            new_row = ""
            for col in range(self.map_size_x):
                if self.map[row][col] == EMPTY:
                    new_row += EMPTY
                else:
                    new_row += self.remove_reachable_rolls(row, col)
            new_map.append(new_row)
        
        return new_map 

    def check_adjacent_rolls(self, row, col):
        adjacents = 0

        if not is_left(col):
            if self.map[row][col-1] == ROLL:
                adjacents += 1
            if not is_top(row):
                if self.map[row-1][col-1] == ROLL:
                    adjacents += 1
            if not is_bottom(row, self.map_size_y):
                if self.map[row+1][col-1] == ROLL:
                    adjacents += 1 
        
        if not is_right(col, self.map_size_x):
            if self.map[row][col+1] == ROLL:
                adjacents += 1
            if not is_top(row):
                if self.map[row-1][col+1] == ROLL:
                    adjacents += 1
            if not is_bottom(row, self.map_size_y):
                if self.map[row+1][col+1] == ROLL:
                    adjacents += 1 
        
        if not is_top(row):
            if self.map[row-1][col] == ROLL:
                adjacents += 1
        
        if not is_bottom(row, self.map_size_y):
            if self.map[row+1][col] == ROLL:
                adjacents += 1

        return adjacents

    def check_reachable_rolls(self, row, col):
        if self.check_adjacent_rolls(row, col) < self.adjacent_threshold:
            self.reachable_rolls += 1
            return REACHABLE
        else:
            return ROLL

    def remove_reachable_rolls(self, row, col):
        if self.check_adjacent_rolls(row, col) < self.adjacent_threshold:
            self.reachable_rolls += 1
            return EMPTY
        else:
            return ROLL

day04 = Day04()
day04.load_map()
day04.print_map()

removed = 0

new_map = day04.check_map_level_2()

while removed != day04.reachable_rolls:
    day04.map = new_map
    removed = day04.reachable_rolls
    new_map = day04.check_map_level_2()

print("New map:")
print_map(new_map)
print(f"Reachable rolls: {day04.reachable_rolls}")