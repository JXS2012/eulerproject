__author__ = 'jianxinsun'

from euler003 import prime_decompose

admicable_set = []



def list_product(l1, l2):
    return [x * y for x in l1 for y in l2]


def get_divisor_sum(n):
    prime_list = prime_decompose(n)
    prime_base = set(prime_list)
    prime_count = dict()
    for i in prime_base:
        prime_count[i] = prime_list.count(i)
    product_list = [[p ** x for x in range(prime_count[p] + 1)] for p in prime_count.keys()]
    divisor_list = [1]
    for l in product_list:
        divisor_list = list_product(divisor_list, l)
    return sum(divisor_list)-n


def check_admicable(a, a_set):
    b = get_divisor_sum(a)
    if b > 0 and a != b and a == get_divisor_sum(b):
        print a
        print b
        a_set.append(a)
        a_set.append(b)


def main():
    upper_bound = 10000
    for i in range(1,upper_bound):
        if i in admicable_set:
            continue
        check_admicable(i, admicable_set)
    print admicable_set
    print sum(admicable_set)


if __name__ == "__main__":
    main()