__author__ = 'jianxinsun'


def pandigital(a,b,c):
    digits = set()
    if len(str(a)) + len(str(b)) + len(str(c)) != 9:
        return False
    for char in str(a):
        digits.add(char)
    for char in str(b):
        digits.add(char)
    for char in str(c):
        digits.add(char)
    if '0' in digits:
        return False
    if len(digits) == 9:
        return True

def main():
    products = set()
    for a in range(1,10):
        for b in range(1000,10000):
            if pandigital(a,b,a*b):
                print a,b,a*b
                products.add(a*b)
    for a in range(10,100):
        for b in range(100,1000):
            if pandigital(a,b,a*b):
                print a,b,a*b
                products.add(a*b)
    print sum(products)


if __name__ == "__main__":
    main()