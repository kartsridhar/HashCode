import math
import re

def readFile(path = "C:/Users/fcb10/Documents/HashCode/2020/d_quite_big.in"):
    with open(path) as f:
        maxSlices, pizzaTypes = list(map(int, f.readline().split()))
        sliceCount = list(map(int, f.readline().split()))
        numberOfSlices = []
        for i in range(pizzaTypes):
            numberOfSlices.append(sliceCount[i])
        f.readline()
    return maxSlices, pizzaTypes, numberOfSlices

# The number of slices are in ascending order of number
# length of numberOfSlices = pizzaTypes
# Need to return the max number of slices possible to order < maxSlices

# Start from the nth slice, increase the sum with the number of slices 
# if it is lesser than the maxSlices.
# keep decrementing the pointer from the last, update temp if the net
# sum is > previous sum && < maxSlices

# Store all the pizza slice count, return the solution with non-zero vals
def solution():
    maxSlices, pizzaTypes, numberOfSlices = readFile()

    pointer1 = pizzaTypes-1

    flag1 = True
    flag2 = True

    sol = []
    score = 0

    while pointer1 >= 0 and flag1 == True:
        temp = []
        pointer2 = pointer1
        maxSum = 0
        while pointer2 >= 0 and flag2 == True:
            maxScore = maxSum + numberOfSlices[pointer2]
            if maxScore < maxSlices:
                maxSum += numberOfSlices[pointer2]
                temp.append(pointer2)
            elif maxScore == maxSlices:
                maxSum += numberOfSlices[pointer2]
                temp.append(pointer2)
                flag1 = False
                flag2 = False
            pointer2 -= 1
        if score < maxSum:
            score = maxSum
            sol = temp
        if pizzaTypes == len(sol):
            flag1 = False
        pointer1 -= 1
    sol.reverse()
    return sol

def writeOut():
    sol = solution()
    out = open("d_quite_big.out", "w")
    out.write(str(len(sol)) + '\n')
    string = ' '.join([str(i) for i in sol])
    out.write(string)

writeOut()

