__author__ = 'jianxinsun'
import time


def main():
    bound = 100
    start = time.time()
    re = set()

    for a in range(2,bound+1):
        for b in range(2,bound+1):
            result = a**b
            re.add(result)

    print len(re)
    print time.time()-start
if __name__=="__main__":
    main()
