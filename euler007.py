__author__ = 'jianxinsun'


import euler003


def isprime(n):
    c = euler003.prime_decompose(n)
    if n in c:
        return True
    else:
        return False

counter = 0
index = 2
while counter < 10001:
    if (isprime(index)):
        index +=1
        counter += 1
    else:
        while not isprime(index):
            index += 1
index -= 1
print index