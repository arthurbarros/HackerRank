import itertools
from fractions import Fraction
b, r = [1], [0]
X = b*3 + r*4
Y = b*4 + r*5
Z = b*4 + r*4

r = [(i)for i in itertools.product(X,Y,Z)]
e = list(map(lambda x : sum(x) == 1,r))
print(Fraction(e.count(True),len(e)))
