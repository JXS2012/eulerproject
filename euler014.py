__author__ = 'jianxinsun'
import pprint
import time

table = [0]

def collatz_next(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n+1

def collatz_reverse_next(n):
    if (n-1) % 3 == 0 and (n-1) % 6 != 0 and n > 4:
        return [(n-1)/3,2*n]
    else:
        return [2*n]


def extend_collatz(l):
    next_collatz_seq = collatz_reverse_next(l[-1])
    if len(next_collatz_seq) == 1:
        return l + next_collatz_seq
    else:
        temp = []
        for item in next_collatz_seq:
            l_copy = l[:]+[item]
            temp.append(l_copy)
        return temp




def generate_collatz(n):
    l = [n]
    while l[-1] != 1:
        l.append(collatz_next(l[-1]))
    return l


def get_collatz_len(n):
    l = n
    length = 0
    while l != 1:
        length += 1
        l = collatz_next(l)
        if l in table.keys():
            table[n] = length+table[l]
            return table[n]
    table[n] = length
    return length

def better_search_longest(n):
    start = time.time()
    max_number = 0
    max_len = 0
    for i in range(n):
        l = i+1
        length = 0
        while l != 1:
            length += 1
            l = collatz_next(l)
            if l<i+1:
                table.append(length+table[l-1])
                break
        if table[i]>max_len:
            max_number = i+1
            max_len = table[i]
    longest = generate_collatz(max_number)
    print max_len
    print longest
    print time.time()-start
    return [max_len,max_number]


def search_longest(n):
    start = time.time()
    max_number = 0
    max_len = 0
    for i in range(n):
        longest = generate_collatz(i+1)
        if len(longest)>max_len:
            max_number = i+1
            max_len = len(longest)
    longest = generate_collatz(max_number)
    print max_len
    print longest
    print time.time()-start
    return [max_len,max_number]



def better_search(bound):
    collatz_map = [[1]]
    dead_collatz_map = []
    while True:
        collatz_map_temp = []
        for item in collatz_map:
            if item[-1]>3*bound+1:
                dead_collatz_map.append(item)
                continue
            new_item = extend_collatz(item)
            if any(isinstance(i, list) for i in new_item):
                collatz_map_temp += new_item
            else:
                collatz_map_temp.append(new_item)
        if collatz_map_temp != []:
            collatz_map = collatz_map_temp
        else:
            break

    dead_collatz_map.reverse()
    for i in range(min([5,len(dead_collatz_map)])):
        next_best = dead_collatz_map[i][:]
        next_best.reverse()
        print (next_best)
        index = 0
        for k in next_best:
            if k<bound:
                next_best = next_best[index:]
                break
            index +=1
        print len(next_best)

