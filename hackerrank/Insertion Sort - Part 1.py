#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(1, n):
        step = i - 1
        key = arr[i]

        while step >= 0 and key < arr[step]:
            arr[step+1] = arr[step]
            print(' '.join(map(str, arr)))
            step -= 1 
        arr[step + 1] = key    
            
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
