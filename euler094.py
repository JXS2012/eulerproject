__author__ = 'jianxinsun'

upper_bound = 1000000000
type_1_bound = (upper_bound-2)/6
type_2_bound = (upper_bound-4)/6
perimeter_sum = 0
for k in range(1,type_1_bound+1):
    height = (3*k**2+4*k+1)**0.5
    if 3*k**2+4*k+1 == int(height)**2:
        print "a = b = {0}, c = {1}, height = {2}, perimeter = {3}".format((2*k+1),2*k,height,6*k+2)
        perimeter_sum += 6*k+2
for k in range(1,type_2_bound+1):
    height = (3*k**2+2*k)**0.5
    if (3*k**2+2*k) == int(height)**2:
        print "a = b = {0}, c = {1}, height = {2}, perimeter = {3}".format((2*k+1),2*k+2,height,6*k+4)
        perimeter_sum += 6*k+4
print perimeter_sum