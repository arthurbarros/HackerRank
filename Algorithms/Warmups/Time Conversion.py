#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if 'AM' in s:
        s = s.replace('AM', '')
        s_arr = s.split(':')
        if s_arr[0] == '12':
            s_arr[0] = '00'
        return ':'.join(s_arr)
    s = s.replace('PM', '')
    s_arr = s.split(':')
    if s_arr[0] != '12':
        s_arr[0] = str(int(s_arr[0]) + 12)
    return ':'.join(s_arr)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
    f.write(result + '\n')

    f.close()
