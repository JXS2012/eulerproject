__author__ = 'jianxinsun'


upper = 2000000
p = 3
index = 2
plist = [i*2+3 for i in range(upper/2-1)]
plist.append(2)

index = 0

while p**2 < upper:
    plist = [x for x in plist if (x==p or x%p!=0)]
    index += 1
    p = plist[index]


print sum(plist)