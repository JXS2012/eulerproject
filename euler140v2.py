__author__ = 'jianxinsun'

nugget = []
b = 10**7
for a in range(1,int(b*(5**0.5-1)/2)):
    num = 3*a*a+a*b
    den = b**2-a**2-a*b
    if num % den == 0:
        z = num/den
        nugget.append(z)
        print z