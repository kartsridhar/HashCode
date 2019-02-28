import numpy as np
import sys

# R (1 ≤ R ≤ 1000) is the number of rows,
# C (1 ≤ C ≤ 1000) is the number of columns,
# L (1 ≤ L ≤ 1000) is the minimum number of each ingredient cells in a slice,
# H (1 ≤ H ≤ 1000) is the maximum total number of cells of a slice

#Tomato = 1 Mushroom = 0

#Reading the input file and returning it as a list
def read_file(filename = sys.argv[1]):
    with open(filename) as f:
        lines = f.readlines()
    lines = [line.rstrip('\n') for line in open(filename)]
    dimensions = lines[0].replace(" ", "")          #replaces the spaces with nothing
    vals = [int(d) for d in str(dimensions)]        #converts the number into a list of digits
    R = vals[0]
    C = vals[1]
    L = vals[2]
    H = vals[3]
    convert = [list(map(lambda t: 1 if t == 'T' else 0, r.strip()))for r in lines[1:]]
    pizza = np.array(convert)
    return R, C, L, H, pizza

R, C, L, H, pizza = read_file()

class Slice(object):
    def __init__(self, r1, c1, r2, c2):     #Constructor for a slice
        self.r1 = r1
        self.c1 = c1
        self.r2 = r2
        self.c2 = c2

    def __size__(self):
        return ((self.r2 - self.r1) + 1) * ((self.c2 - self.c1) + 1)

    def __getTomatoCount__(self):
        count = 0
        for i in range(self.r1, self.r2 + 1):
            for j in range(self.r2, self.c2 + 1):
                count += pizza[i][j] == 1
            return count

    def __check__(self):
        tomato = self.__getTomatoCount__()
        mushroom = self.__size__() - tomato
        length = tomato >= L and mushroom >= L
        height = tomato + mushroom <= H
        return length and height
