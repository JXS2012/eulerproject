__author__ = 'jianxinsun'
import time

def read_sudoku(filename):
    f = open(filename,'r')

    text = f.readlines()

    sudoku_index = -1
    sudoku_data = []
    for line in text:
        if line.split()[0] == 'Grid':
            sudoku_data.append([])
            sudoku_index += 1
        else:
            sudoku_data[sudoku_index].append([int(digit) for digit in line.rstrip('\n')])
    f.close()
    return sudoku_data


def init_candidate(unknown_slots):
    candidates = dict()
    for i in unknown_slots:
        candidates[i] = [j+1 for j in range(9)]
    return candidates


def update_candidate(sudoku,candidates,unknown_slots):
    sudoku_copy=[]
    for i in sudoku:
        sudoku_copy.append(i[:])
    candidates_copy = candidates.copy()
    unknown_slots_copy = unknown_slots[:]
    changed = True
    while changed:
        changed = False
        for i in unknown_slots_copy:
            candidates_copy[i] = filter_candidate(sudoku_copy,i,candidates_copy[i])
            if len(candidates_copy[i]) == 1:
                sudoku_copy = update_sudoku(sudoku_copy,i,candidates_copy[i])
                unknown_slots_copy.remove(i)
                del candidates_copy[i]
                changed = True
    return (sudoku_copy,candidates_copy,unknown_slots_copy)


def filter_candidate(sudoku,i,candidate):
    candidate_temp = filter_row(sudoku,i[0],candidate)
    candidate_temp = filter_column(sudoku,i[1],candidate_temp)
    candidate_temp = filter_square(sudoku,i,candidate_temp)
    return candidate_temp

def filter_row(sudoku, row, candidate):
    candidate_temp=candidate[:]
    conflict_set = set(sudoku[row])
    for k in conflict_set:
        candidate_temp = [x for x in candidate_temp if x != k]
    return candidate_temp


def filter_column(sudoku, column, candidate):
    conflict_set = set([sudoku[j][column] for j in range(9)])
    candidate_temp = candidate[:]
    for k in conflict_set:
        candidate_temp = [x for x in candidate_temp if x != k]
    return candidate_temp

def filter_square(sudoku, i, candidate):
    candidate_temp=candidate[:]
    square_row = i[0]/3*3
    square_column = i[1]/3*3
    square = set([sudoku[j][k] for j in range(square_row, square_row+3) for k in range(square_column, square_column+3)])
    for k in square:
        candidate_temp = [x for x in candidate_temp if x != k]
    return candidate_temp

def update_sudoku(sudoku,i,correct_value):
    sudoku_temp = []
    for k in sudoku:
        sudoku_temp.append(k[:])
    sudoku_temp[i[0]][i[1]] = correct_value[0]
    return sudoku_temp


def search_solution(sudoku, candidates, unknown_slots):
    if unknown_slots == []:
        return (sudoku, True)
    else:
        sudoku_copy=[]
        for i in sudoku:
            sudoku_copy.append(i[:])
        candidates_copy = candidates.copy()
        unknown_slots_copy = unknown_slots[:]
        (sudoku_copy, candidates_copy, unknown_slots_copy) = update_candidate(sudoku,candidates,unknown_slots)
        if unknown_slots_copy == []:
            return (sudoku_copy, True)
        for i in candidates_copy.keys():
            if candidates_copy[i] == []:
                return (sudoku, False)

        min_no_candidate = 9
        min_candidate = []
        min_candidate_pos = ()
        for i in unknown_slots_copy:
            if min_no_candidate > len(candidates_copy[i]):
                min_no_candidate = len(candidates_copy[i])
                min_candidate = candidates_copy[i]
                min_candidate_pos = i
            if min_no_candidate == 1:
                break

        sudoku_sol = []
        solve = False
        for i in min_candidate:
            sudoku_temp = update_sudoku(sudoku_copy,min_candidate_pos,[i])
            candidates_temp = candidates_copy.copy()
            del candidates_temp[min_candidate_pos]
            unknown_slots_temp = unknown_slots_copy[:]
            unknown_slots_temp.remove(min_candidate_pos)
            (sudoku_sol,solve) = search_solution(sudoku_temp,candidates_temp,unknown_slots_temp)
            if solve:
                break
        return(sudoku_sol,solve)


def find_unknown_slots(sudoku):
    row = 0
    column = 0
    unknown_slots=[]
    for x in sudoku:
        for y in x:
            if y == 0:
                unknown_slots.append((row,column))
            column += 1
        row += 1
        column = 0
    return unknown_slots

def solve_sudoku(sudoku):
    unknown_slots = find_unknown_slots(sudoku)
    candidates = init_candidate(unknown_slots)

    #while unknown_slots != []:
    #    (sudoku, candidates, unknown_slots, changed) = update_candidate(sudoku,candidates,unknown_slots)
    (sudoku,solve)= search_solution(sudoku,candidates,unknown_slots)

    return (sudoku,solve)


def main():
    data = read_sudoku('euler096sudoku.txt')
    sum_sudoku = 0
    (answer, solve) = solve_sudoku(data[4])
    print solve
    for i in answer:
        print i

    start = time.time()
    for i in range(len(data)):
        (answer, solve) = solve_sudoku(data[i])
        print "Grid%d"%(i+1)
        for i in answer:
            print i
        sum_sudoku += answer[0][0]*100+answer[0][1]*10+answer[0][2]
    print sum_sudoku
    print time.time()-start

if __name__=="__main__":
    main()