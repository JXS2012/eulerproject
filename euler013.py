__author__ = 'jianxinsun'


f = open('euler013digits.txt','r')

text = f.readlines()
digits = []
for line in text:
    digits.append(int(line[0:11]))
print sum(digits)
