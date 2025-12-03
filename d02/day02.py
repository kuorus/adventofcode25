
import re

class Day02:

    def __init__(self):
        self.ranges = []
        self.solution = 0

    def loadList(self):
        with open("input.dat", "r") as file:
            self.ranges = file.read().split(',')

    def loadAltList(self):
        with open("test.dat", "r") as file:
            self.ranges = file.read().split(',')

    def printRanges(self):
        print(self.ranges)

    def checkDouble(self, number):
        num_to_str = str(number)
        if len(num_to_str) % 2 != 0:
            return False
        else:
            pairs = (num_to_str[0:len(num_to_str)//2], num_to_str[len(num_to_str)//2:])
            return pairs[0] == pairs[1]

    def iterateRangesLevel1(self):
        for range_str in self.ranges:
            self.iterateRangeLevel1(range_str)

    def iterateRangesLevel2(self):
        for range_str in self.ranges:
            self.iterateRangeLevel2(range_str)

    def iterateRangeLevel1(self, range_str):
        range_int = range_str.split('-')
        for num in range(int(range_int[0]), int(range_int[1])+1):
            if self.checkDouble(str(num)):
                self.solution += num


    def iterateRangeLevel2(self, range_str):
        range_int = range_str.split('-')
        for num in range(int(range_int[0]), int(range_int[1])+1):
            if self.checkRepeating(str(num)):
                self.solution += num

    def checkRepeating(self, number):
        for x in range(1, len(number)//2 + 1):
            subs = re.sub(number[0:x], "", number)
            if subs == '':
                return True

d2 = Day02()
d2.loadList()
#d2.printRanges()
#d2.loadAltList()
d2.iterateRangesLevel1()
print(f"The solution is: {d2.solution}")
d2.solution = 0
d2.iterateRangesLevel2()
print(f"The solution is: {d2.solution}")