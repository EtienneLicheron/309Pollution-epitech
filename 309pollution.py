#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## B-MAT-500-MPL-5-1-309pollution-etienne.licheron
## File description:
## 309pollution
##

import sys

from math import factorial

def getContent(filename):
    with open(filename, 'r') as f:
        return [elem.replace('\n', '') for elem in f.readlines()]

def createMap(n, fileContent):
    map = [[0 for i in range(n)] for j in range(n)]
    for elem in fileContent:
        map[elem[0]][elem[1]] = elem[2]
    return map

def coefficientBinomial(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))

def bezier(n, coords, k):
    return pow(coords/n, k) * pow(1 - (coords/n), n-k)

def computePollution(n, x, y, map):
    pollution = 0
    for i in range(n):
        for j in range(n):
            pollution += map[i][j] * coefficientBinomial(n-1, i) * coefficientBinomial(n-1, j) * bezier(n-1, x, i) * bezier(n-1, y, j)
    print('{:.2f}'.format(pollution))

def runPollution(args):
    n = int(args[1])
    fileContent = getContent(args[2])
    x = float(args[3])
    y = float(args[4])
    fileContent = [[int(elem.split(';')[0]), int(elem.split(';')[1]), float(elem.split(';')[2])] for elem in fileContent]
    computePollution(n, x, y, createMap(n, fileContent))

def print_help():
    print("USAGE\n\t./309pollution n file x y\nDESCRIPTION\n\tn\tnumber of points on the grid axis\n\tfile\tcsv file containing the data points x;y;p\n\tx\tabscissa of the point whose pollution level we want to know\n\ty\tordinate of the point whose pollution level we want to know")

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        print_help()
        exit(0)
    if len(sys.argv) != 5:
        exit(84)
    runPollution(sys.argv)

if __name__ == "__main__":
    main()