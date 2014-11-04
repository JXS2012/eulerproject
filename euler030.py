__author__ = 'jianxinsun'
import time


start = time.time()
n=1
while (9**5*n>10**n):
    n+=1
print n-1

l = []
for i in range(2,10**n):
    temp = i
    tot = 0
    while temp!=0:
        tot += (temp%10)**5
        temp /= 10
    if tot == i:
        l.append(i)
    #if sum([int(c)**5 for c in str(i)]) == i:
    #   l.append(i)
print sum(l)
print l
print time.time()-start

from time import *

start = clock()

max = 10
l = []
for a in range(0, max):
    for b in range(0, max):
        for c in range(0, max):
            for d in range(0, max):
                for e in range(0, max):
                    for f in range(0, max):
                        if a**5 + b**5 + c**5 + d**5 + e**5 + f**5 == f + e*10 + d*100 + c*1000 + b*10000 + a*100000:
                            l.append(f*1 + e*10 + d*100 + c*1000 + b*10000 + a*100000)

print(sum(l)-1)

print(clock()-start)