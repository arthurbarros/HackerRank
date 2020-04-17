# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

text = sys.stdin.readlines()
X = [int(x) for x in text[1].replace('\n', '').split(' ')]
W = [int(x) for x in text[2].replace('\n', '').split(' ')]

X_W = sum([ X[i]*W[i] for i in range(len(X))])
print(round(X_W / sum([int(x) for x in W]),1))
