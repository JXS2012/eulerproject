__author__ = 'jianxinsun'


max = 100

squaresum = sum([(i+1)**2 for i in range(max)])
sumsquare = (sum([i+1 for i in range(max)]))**2
diff = sumsquare-squaresum
print diff