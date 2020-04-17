# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

text = sys.stdin.readlines()[1:][0]
list_el = [ float(x) for x in text.split(' ')]

mean = sum(list_el) / len(list_el)

list_el.sort()
mid = len(list_el) // 2
meadian = (list_el[mid] + list_el[~mid]) / 2

print(mean)
print(meadian)
print(max(list_el, key = list_el.count))
