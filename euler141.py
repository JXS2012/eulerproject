__author__ = 'jianxinsun'

import gmpy

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

l = set()

for a in range(2,10**4):
    for b in range(1,a):
        if gcd(a,b) > 1:
            continue
        n = a**3*b+b**2
        c = 1
        if n > 10 ** 12:
            break
        if gmpy.is_square(n):
            print n
            l.add(n)
        while n < 10**12:
            c += 1
            n = c**2*a**3*b+c*b**2
            if gmpy.is_square(n):
                l.add(n)
                print n

print sum(l)
