__author__ = 'jianxinsun'
import time

total = 10000
c_value = [1,2,5,10,20,50,100,200]
memo = [[0 for x in range(1,8)] for y in range(total+1)]

def fast_search(amount):
    ways = [0 for a in range(total+1)]
    ways[0] = 1
    for i in range(8):
        for j in range(c_value[i],amount+1):
            ways[j] += ways[j-c_value[i]]
    print ways[amount]


def search_remain(remain,i):
    if i <= 0:
        return 1
    partial_sum = 0
    remain_copy = remain
    if memo[remain_copy][i-1] > 0:
        partial_sum = memo[remain_copy][i-1]
        return partial_sum
    while remain >= 0:
        partial_sum += search_remain(remain,i-1)
        remain -= c_value[i]
    memo[remain_copy][i-1] = partial_sum
    return partial_sum

start = time.time()
total_division = search_remain(total,7)
print total_division
print time.time()-start

start = time.time()
fast_search(total)
print time.time()-start