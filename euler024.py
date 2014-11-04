__author__ = 'jianxinsun'
import math
import time


start = time.time()
bound = 1000000-1

digits = [0,1,2,3,4,5,6,7,8,9]
results = []
for i in reversed(range(10)):
    results.append(digits[bound/math.factorial(i)])
    del digits[bound/math.factorial(i)]
    bound %= math.factorial(i)
print results
s = ''.join([str(x) for x in results])
print s
print (time.time()-start)*1000