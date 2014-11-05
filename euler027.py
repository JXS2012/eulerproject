__author__ = 'jianxinsun'
import time


def is_prime(n):
    return sum([1 for j in range(2,int(n**0.5)+1) if n%j == 0]) == 0


def find_largest_seq(a,b):
    n = 0
    while n**2+a*n+b>0 and is_prime(n**2+a*n+b):
        n += 1
    return n

def main():
    start = time.time()
    b_list = []
    for i in range(2,1000):
        if is_prime(i):
            b_list.append(i)
    print b_list
    max_seq = 0
    max_product = 0
    for b in b_list:
        if b == 2:
            a_list = [2*x for x in range(-36,500)]
        else:
            a_list = [2*x + 1 for x in range(max(-1000/2,(-71-b/79)/2),1000/2)]
        for a in a_list:
            temp = find_largest_seq(a,b)
            if temp > max_seq:
                max_seq = temp
                max_product = a*b
    print max_seq
    print max_product
    print time.time()-start


if __name__ == "__main__":
    main()

