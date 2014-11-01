__author__ = 'jianxinsun'
import euler003

divisor_no = 0
triangle_index = 23
threshold = 500
while divisor_no <= threshold:
    triangle_no = triangle_index*(triangle_index+1)/2
    prime_total = euler003.prime_decompose(triangle_no)
    prime_total = [x for x in prime_total if x != 1]
    prime_set = set(prime_total)
    prime_count = dict()
    for p in prime_set:
        prime_count[p] = prime_total.count(p)
    divisor_no = 1
    for p in prime_count.keys():
        divisor_no *= prime_count[p]+1
    triangle_index += 1

print 0.5*triangle_index*(triangle_index-1)