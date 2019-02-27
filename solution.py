import numpy as np
import sys
from enum import Enum

class Toppings(Enum):
    T = 0
    M = 1
# R (1 ≤ R ≤ 1000) is the number of rows,
# C (1 ≤ C ≤ 1000) is the number of columns,
# L (1 ≤ L ≤ 1000) is the minimum number of each ingredient cells in a slice,
# H (1 ≤ H ≤ 1000) is the maximum total number of cells of a slice

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
    toppings = np.array(convert)
    return R, C, L, H, toppings

read_file()
#Each character is either M or T (Mushroom or Tomato)

#Idea 1:
#choose any random start point that is available
#enter a random shape size and fit to location chosen
#check constraints and update the available cells
#check again, if doesn't exist, stop.
