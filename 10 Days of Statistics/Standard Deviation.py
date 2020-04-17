# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import math

arr = [int(x) for x in sys.stdin.readlines()[1:][0].split()]
mean = sum(x for x in arr) / len(arr)
sqr_distance = (sum((x-mean)**2 for x in arr) / len(arr))
print('{:.1f}'.format(math.sqrt(sqr_distance)))
