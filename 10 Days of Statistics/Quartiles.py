# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

arr = [int(x) for x in sys.stdin.readlines()[1:][0].split()]
arr.sort()


def quartile(arr):
    if not len(arr) % 2 == 0:
        lower_half = arr[:len(arr)//2]
        upper_half = arr[1+len(arr)//2:]
        res = arr[len(arr)//2]
    else:
        lower_half = arr[:len(arr)//2]
        upper_half = arr[len(arr)//2:]
        res = (lower_half[-1] + upper_half[0]) / 2
    return res, lower_half, upper_half


q1, lower_25, upper_25 = quartile(lower_half)
q2, lower_half, upper_half = quartile(arr)
q3, lower_50, upper_50 = quartile(upper_half)

print(int(q1))
print(int(q2))
print(int(q3))
