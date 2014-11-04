__author__ = 'jianxinsun'
import euler021
import time

upper = 28123
abundant_list = []
start = time.time()
for i in range(upper):
    if euler021.get_divisor_sum(i+1)>i+1:
        abundant_list.append(i+1)
abundant_sum_set = set([x+y for x in abundant_list for y in abundant_list if x+y<=upper])
print abundant_sum_set
non_abundant_list = []
for i in range(upper):
    if not ((i+1) in abundant_sum_set):
        non_abundant_list.append(i+1)
print time.time()-start
print non_abundant_list
print sum(non_abundant_list)