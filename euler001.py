__author__ = 'jianxinsun'

sum = 0
upper = 1000-1
for i in range(upper/3):
    sum += (i+1)*3
print sum
for i in range(upper/5):
    sum += (i+1)*5
print sum
for i in range(upper/15):
    sum -= (i+1)*15
print sum
