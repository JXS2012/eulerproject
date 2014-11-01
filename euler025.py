__author__ = 'jianxinsun'
import euler002
import math

n = 1
f1 = 0
f2 = 1
f = f1+f2
while math.log10(f)<999:
    f = f1 + f2
    f1 = f2
    f2 = f
    n+=1
print n