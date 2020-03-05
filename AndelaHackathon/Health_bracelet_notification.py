#!/bin/python3

import math
import os
import random
import re
import sys
# import time
# from statistics import median

#
# Complete the 'activityAlerts' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY distances
#  2. INTEGER d
#

# def isNotify(median, user_miles):
#     return user_miles >= median * 2
def median(data):
    data.sort()
    mid = len(data) // 2
    return (data[mid] + data[~mid]) / 2

def activityAlerts(distances, d, n):
    
    # norm_distances = [distances[idx] for idx in range(n)]
    notification = 0
    start_day = 0
    stop_day = d
    index1 = 0
    lastIndex = d
    occurrences = [0] * len(distances)
    trailing_data = []
    # trailing_data = [0] * d
    user_miles = 0
    for key, value in enumerate(distances[d:]):
        # tt = time.time()
        trailing_data = distances[start_day:stop_day]
        # print('<<--->', time.time() - tt)
        user_miles = distances[stop_day]
        # t = time.time()
        median_value = median(trailing_data)
        # print('--->', time.time() - t)
        start_day +=1
        stop_day +=1
        if (user_miles >= median_value * 2):
            notification += 1
    return notification
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # start_time = time.time()

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    distances = list(map(int, input().rstrip().split()))

    result = activityAlerts(distances, d, n)

    fptr.write(str(result) + '\n')
    

    fptr.close()
    # print('ends', time.time() - start_time)