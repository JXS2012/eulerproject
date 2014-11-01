__author__ = 'jianxinsun'
import re


def get_column(digits, x, y, d):
    return [digits[x + j][y] for j in range(d)]


def get_row(digits, x, y, d):
    return [digits[x][y + j] for j in range(d)]


def get_diagonal(digits,x,y,d):
    return [digits[x+j][y+j] for j in range(d)]


def get_rdiagonal(digits,x,y,d):
    return [digits[x+j][y-j] for j in range(d)]


def get_product(l):
    prod = 1
    for k in l:
        prod *= k
    return prod


f = open('euler011digits.txt', 'r')

text = f.readlines()
digits = []
dist = 4
for item in text:
    row = item[:-1].split(' ')
    digits_row = [int(j) for j in row]
    digits.append(digits_row)
print get_rdiagonal(digits,0,3,4)
max_prod = 0
for row in range(len(digits)-dist+1):
    for column in range(len(digits[0])-dist + 1):
        max_prod = max([get_product(get_column(digits, row, column, dist)),
                        get_product(get_row(digits, row, column, dist)),
                        get_product(get_diagonal(digits, row, column, dist)),
                        max_prod])
print max_prod
for row in range(len(digits)-dist+1):
    for column in range(dist-1,len(digits[0])):
        max_prod = max([max_prod,
                       get_product(get_rdiagonal(digits, row, column, dist))])
print max_prod