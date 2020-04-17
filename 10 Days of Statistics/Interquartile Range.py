# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 

lines = sys.stdin.readlines()

def cast_line_arr_int(line):
    return [int(x) for x in line.split()]

def shape_S(X, F):
    S = []
    for i in range(0, len(X)):
        S += [X[i] for _ in range(F[i])]
    return S

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


X = cast_line_arr_int(lines[1])
F = cast_line_arr_int(lines[2])
S = shape_S(X,F)
S.sort()

q2, lower_half, upper_half = quartile(S)
q1, lower_25, upper_25 = quartile(lower_half)
q3, lower_50, upper_50 = quartile(upper_half)

interquartile_rage = q3 - q1

print('{:.1f}'.format(interquartile_rage))
