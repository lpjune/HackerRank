#!/bin/python3

import os
import sys


#
# Complete the howManyStudents function below.
# my code starts
def howManyStudents(m, c):
    s = []                     # empty list s
    dic = {}                   # empty dictionary dic
    for i in range(m):         # for each number in m
        num = c.count(i)       # num is how many times that number is in c
        dic[i] = num           # add dic key of i, with value num
    for value in dic.values(): # for each value in dic
        s.append(value)        # add it to list s
    return s                   # return s
# my code ends


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = howManyStudents(m, c)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
