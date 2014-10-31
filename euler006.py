__author__ = 'jianxinsun'


def palindromic_check(n):
    s = str(n)
    k = 0
    while (k<len(s)/2 and s[k] == s[-k-1]):
        k += 1
    if k >= len(s)/2:
        return True
    else:
        return False

def main():
    palindromic_list = []
    for i in reversed(range(100,1000)):
        for j in reversed(range(100,1000)):
            if palindromic_check(i * j):
                #print "{0} X {1} = {2}".format(i,j,i*j)
                palindromic_list.append(i*j)
    print max(palindromic_list)

if __name__ == "__main__":
    main()