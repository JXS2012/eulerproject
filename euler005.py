__author__ = 'jianxinsun'


import euler003


max_index = 20
primelists = dict()
temp = []
for i in range(max_index):
    primelists[i] = euler003.prime_decompose(i+1)
    temp += primelists[i]
primeset = set(temp)

primecount = dict()
for item in primeset:
    primecount[item] = max([primelists[i].count(item) for i in range(max_index)])

lowest_product = 1
for item in primeset:
    lowest_product *= item**primecount[item]

print lowest_product