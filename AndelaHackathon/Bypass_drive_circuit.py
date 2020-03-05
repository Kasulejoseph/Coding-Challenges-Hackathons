#!/bin/python3

import math
import os
import random
import re
import sys
from operator import itemgetter

#
# Complete the 'bypassCircuit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY stations as parameter.
#

def bypassCircuit(stations):
    # Write your code here
    petrol = [0]* len(stations)
    distance = [0]* len(stations)
    sumPetrol = 0
    sumDistance = 0
    index1 = 0
    index2 = 0
    for key, station in enumerate(stations):
        petrol[key] = station[0]
        distance[key]= station[1]
    while(index1 < len(petrol)):
        sumPetrol += petrol[index1] 
        sumDistance += distance[index1]
        while(sumDistance > sumPetrol):
            sumPetrol -= petrol[index2] 
            sumDistance -= distance[index2]
            petrol[index2] = petrol[index2 +1]
            distance[index2] = distance[index2 + 1]
            index2 += 1 
        index1 += 1 
    return index2
            
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    stations = []

    for _ in range(n):
        stations.append(list(map(int, input().rstrip().split())))

    result = bypassCircuit(stations)

    fptr.write(str(result) + '\n')

    fptr.close()