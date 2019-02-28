import numpy as np
import sys

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

cut_pizza = []

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
            for j in range(self.c1, self.c2 + 1):
                count += pizza[i][j] == 1
            return count

    def __check__(self):
        tomato = self.__getTomatoCount__()
        mushroom = self.__size__() - tomato
        length = tomato >= L and mushroom >= L
        height = tomato + mushroom <= H
        return length and height

#function to find the best slice given a start and end point
def best_slice(r1, r2, _slice):
    c1 = 0
    total = 0
    while (c1 < C):
        c2 = c1                     #start with slice consisting only 1 column
        checkBefore = False
        while (c2 < C):
            if (Slice(r1, c1, r2, c2).__check__()):     #check if the slice is delimited by r1, r2
                checkBefore = True
            elif (checkBefore == True):
                _slice = np.append(_slice, Slice(r1, c1, r2, c2 - 1))       #if condition is true, push the previous slice to the list
                total += len(_slice[-1])        #reference the last element of a list
                break
            c2 += 1
        if (checkBefore == False):          #cant create any slice from this column. skip this, start with the next
            c1 += 1
        else:
            c1 = c2
    return total

def find_pizza_cut():
    r1 = 0
    while (r1 < R):                 #Continue the algo while there is an empty row availaible
        r2 = r1, bestVal = -1        #start with r2 = r1
        slice1 = []
        while (r2 < R):
            slice2 = []
            res = best_slice(r1, r2, slice2)        #returns the best solution of row range r1-r2
            if (res < bestVal):
                r2 -= 1
                break
            bestVal = res
            slice1 = slice2
            r2 += 1
        for i in len(slice2):
            cut_pizza = np.append(cut_pizza, slice2[i])
        r1 = r2 + 1

# find_pizza_cut()
# out = open("output_example.txt", "w+")
# out.write(str())
def main():
    find_pizza_cut()
    out = open("a_example_out.txt", "w+")
    out.write(str() + "\n")
    for cut in cut_pizza:
        out.write("%d %d %d %d \n" % (cut_pizza[0], cut_pizza[1], cut_pizza[2], cut_pizza[3]))
    print(cut_pizza)
