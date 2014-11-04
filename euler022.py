__author__ = 'jianxinsun'
import time


def get_name_score(name,multiplier):
    score = 0
    for char in name:
        score += ord(char)-ord('A')+1
    return score * multiplier


start = time.time()
f = open("euler022names.txt",'r')
text = f.readline()
names = sorted([name.strip('"') for name in text.split(',')])
total = 0

for multiplier in range(len(names)):
    total += get_name_score(names[multiplier],multiplier+1)

print time.time()-start
print total