__author__ = 'jianxinsun'




def decompose(m):
    for i in reversed(range(int(m**0.5)+1)):
        if (m % i == 0):
            #print "{0} = {1} X {2}".format(m, i, m/i)
            return [i, m/i]


def prime_decompose(m):
    [a,b] = decompose(m)
    if (a == 1):
        return [b]
    else:
        return prime_decompose(a) + prime_decompose(b)


def main():
    a = 300

    c = prime_decompose(a)

    print c


if __name__=='__main__':
    main()