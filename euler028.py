__author__ = 'jianxinsun'

total = 1
level = 1001
kmax = (level+1)/2
for k in range(2,kmax+1):
    a = (2*k-1)**2
    b = a - 2*k + 2
    c = b - 2*k + 2
    d = c - 2*k + 2
    total += a+b+c+d
print total
