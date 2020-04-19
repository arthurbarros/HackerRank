import itertools
from fractions import Fraction
# 1: red 2: blue
S = [[1], [1], [1], [2], [2], [2], [2]]
SDRAW = S[1:]

e = list(map(lambda x : sum(x) == 2,SDRAW))
print(Fraction(e.count(True),len(SDRAW)))
