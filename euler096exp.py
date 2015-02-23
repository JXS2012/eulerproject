__author__ = 'jianxinsun'
import time
import copy


def read_sudoku(filename):
    f = open(filename, 'r')

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
        candidates[i] = [j + 1 for j in range(9)]
    return candidates


def consistency_checking(sudoku, candidates, unknown_slots):
    changed = True
    while changed:
        changed = False
        for i in unknown_slots:
            filter_candidate(sudoku, i, candidates[i])
            if len(candidates[i]) == 1:
                update_sudoku(sudoku, i, candidates[i])
                unknown_slots.remove(i)
                del candidates[i]
                changed = True


def filter_candidate(sudoku, i, candidate):
    conflict_set = get_conflict_set(sudoku,i)
    for k in conflict_set:
        if k in candidate:
            candidate.remove(k)
    # filter_row(sudoku, i[0], candidate)
    # filter_column(sudoku, i[1], candidate)
    # filter_square(sudoku, i, candidate)

def get_conflict_set(sudoku,i):
    conflict = sudoku[i[0]][:]
    conflict += [sudoku[j][i[1]] for j in range(9)]
    square_row = i[0] / 3 * 3
    square_column = i[1] / 3 * 3
    conflict += [sudoku[j][k] for j in range(square_row, square_row + 3) for k in range(square_column, square_column + 3)]
    conflict_set = set(conflict)
    return conflict_set


def filter_row(sudoku, row, candidate):
    conflict_set = set(sudoku[row])
    for k in conflict_set:
        if k in candidate:
            candidate.remove(k)


def filter_column(sudoku, column, candidate):
    conflict_set = set([sudoku[j][column] for j in range(9)])
    for k in conflict_set:
        if k in candidate:
            candidate.remove(k)


def filter_square(sudoku, i, candidate):
    square_row = i[0] / 3 * 3
    square_column = i[1] / 3 * 3
    square = set([sudoku[j][k] for j in range(square_row, square_row + 3) for k in range(square_column, square_column + 3)])
    for k in square:
        if k in candidate:
            candidate.remove(k)


def update_sudoku(sudoku, i, correct_value):
    sudoku[i[0]][i[1]] = correct_value[0]


def backtracking(sudoku, candidates, unknown_slots, level):
    if unknown_slots == []:
        print level
        return (sudoku, True)
    else:
        consistency_checking(sudoku, candidates, unknown_slots)
        if unknown_slots == []:
            print level
            return (sudoku, True)
        for i in candidates.keys():
            if candidates[i] == []:
                return (sudoku, False)

        min_no_candidate = 9
        min_candidate = []
        min_candidate_pos = ()
        for i in unknown_slots:
            if min_no_candidate > len(candidates[i]):
                min_no_candidate = len(candidates[i])
                min_candidate = candidates[i]
                min_candidate_pos = i
            if min_no_candidate == 1:
                break

        sudoku_sol = []
        solve = False
        for i in min_candidate:
            sudoku_temp = []
            for k in sudoku:
                sudoku_temp.append(k[:])
            update_sudoku(sudoku_temp, min_candidate_pos, [i])
            candidates_temp = dict()
            for k in candidates:
                candidates_temp[k] = candidates[k][:]
            del candidates_temp[min_candidate_pos]
            unknown_slots_temp = unknown_slots[:]
            unknown_slots_temp.remove(min_candidate_pos)
            level += 1
            (sudoku_sol, solve) = backtracking(sudoku_temp, candidates_temp, unknown_slots_temp, level)
            if solve:
                break
        return (sudoku_sol, solve)


def find_unknown_slots(sudoku):
    row = 0
    column = 0
    unknown_slots = []
    for x in sudoku:
        for y in x:
            if y == 0:
                unknown_slots.append((row, column))
            column += 1
        row += 1
        column = 0
    return unknown_slots


def solve_sudoku(sudoku):
    unknown_slots = find_unknown_slots(sudoku)
    candidates = init_candidate(unknown_slots)

    # while unknown_slots != []:
    #    (sudoku, candidates, unknown_slots, changed) = update_candidate(sudoku,candidates,unknown_slots)
    (sudoku, solve) = backtracking(sudoku, candidates, unknown_slots, 0)

    return (sudoku, solve)


def main():
    data = read_sudoku('euler096sudoku.txt')
    sum_sudoku = 0

    result = True
    start = time.time()
    for i in range(len(data)):
        print "Grid%d"%(i+1)
        (answer, solve) = solve_sudoku(data[i])
        result = solve and result
        sum_sudoku += answer[0][0] * 100 + answer[0][1] * 10 + answer[0][2]
    print sum_sudoku
    print result
    print time.time() - start


if __name__ == "__main__":
    main()