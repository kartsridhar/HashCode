import numpy as np
import sys
# R (1 ≤ R ≤ 1000) is the number of rows,
# C (1 ≤ C ≤ 1000) is the number of columns,
# L (1 ≤ L ≤ 1000) is the minimum number of each ingredient cells in a slice,
# H (1 ≤ H ≤ 1000) is the maximum total number of cells of a slice
def read_file(filename):
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readLines()
    lines = [line.rstrip('\n') for line in open(filename)]
#Each character is either M or T (Mushroom or Tomato)

#Idea 1:
#choose any random start point that is available
#enter a random shape size and fit to location chosen
#check constraints and update the available cells
#check again, if doesn't exist, stop.
