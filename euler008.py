__author__ = 'jianxinsun'


def get_row(digits, x, d):
    return [digits[x + j] for j in range(d)]


f = open('euler008digits.txt', 'r')

text = f.readlines()
digits = []

for item in text:
    index = 0
    digits_row = []
    while (index < len(item)) and (item[index] != '\n'):
        digits_row.append(int(item[index]))
        index += 1
    digits += digits_row

dist = 13
max_product = 0


def get_product(l):
    prod = 1
    for k in l:
        prod *= k
    return prod


prod_dict = dict()

for i in range(len(digits) - dist + 1):
    max_product = max([get_product(get_row(digits, i, dist)), max_product])
print max_product
