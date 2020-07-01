# Hackerrank Problem
#!/bin/python3

import math
import os
import random
import re
import sys

# The migratoryBirds function is as follows:
def migratoryBirds(arr,n):
    arr_freq=[0,0,0,0,0,0]
    for j in range(0,len(arr_freq)):
        for i in range(0,n):
            if(j == arr[i]):
                arr_freq[j]=arr_freq[j]+1
    k=max(arr_freq)
    return (arr_freq.index(k))

# Main Program Starts here:
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr,arr_count)

    fptr.write(str(result) + '\n')

    fptr.close()
