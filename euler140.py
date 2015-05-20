__author__ = 'jianxinsun'

import gmpy
k = 0
golden_nugget = [2, 5, 21, 42, 152, 296, 1050, 2037, 7205, 13970, 49392, 95760, 338546, 656357, 2320437, 4498746, 15904520, 30834872, 109011210, 211345365, 747173957]
z = golden_nugget[-1] + 1
while k < 9:
    #to solving Ag: Ag-xAg = G1*x + (G2-G1)*x^2 + x^2Ag
    #equivalent to (Ag+3)x^2 + (Ag+1)x - Ag = 0
    n = (z+1)**2+4*z*(z+3)
    if gmpy.is_square(n):
        golden_nugget.append(z)
        k += 1
        print z
    z += 1
print golden_nugget