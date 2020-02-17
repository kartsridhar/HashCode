import math
import re

def readFile(path):
    path = path + ".in"
    with open(path) as f:
        maxSlices, pizzaTypes = list(map(int, f.readline().split()))
        sliceCount = list(map(int, f.readline().split()))
        numberOfSlices = []
        for i in range(pizzaTypes):
            numberOfSlices.append(sliceCount[i])
        f.readline()
    return maxSlices, pizzaTypes, numberOfSlices

# Store all the pizza slice count, return the solution with non-zero vals
def solution(maxSlices, pizzaTypes, numberOfSlices):
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

def writeOut(path):
    maxSlices, pizzaTypes, numberOfSlices = readFile(path)
    sol = solution(maxSlices, pizzaTypes, numberOfSlices)
    path = path + ".out"
    out = open(path, "w")
    out.write(str(len(sol)) + '\n')
    string = ' '.join([str(i) for i in sol])
    out.write(string)

def run():
    fileNames = ["a_example", "b_small", "c_medium", "d_quite_big", "e_also_big"]
    for i in range(len(fileNames)):
        maxSlices, pizzaTypes, numberOfSlices = readFile(fileNames[i])
        sol = solution(maxSlices, pizzaTypes, numberOfSlices)
        writeOut(fileNames[i])

run()