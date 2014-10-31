__author__ = 'jianxinsun'


phi = (5**0.5+1)/2

def fib(n):
    return (phi**n-(-phi)**(-n))/(5**0.5)

sum = 0
index = 3
while fib(index) < 4e6:
    sum += fib(index)
    index += 3
print sum