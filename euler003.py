__author__ = 'jianxinsun'




def decompose(m):
    for i in range(int(m**0.5)):
        if (m % (int(m**0.5)-i) == 0):
            #print "{0} = {1} X {2}".format(m,int(m**0.5)-i,m/(int(m**0.5)-i))
            return [int(m**0.5)-i,m/(int(m**0.5)-i)]


def prime_decompose(m):
    [a,b] = decompose(m)
    if (a == 1):
        return [b]
    else:
        return decompose(a) + decompose(b)


def main():
    a = 600851475143

    c = prime_decompose(a)

    #print c


if __name__=='__main__':
    main()