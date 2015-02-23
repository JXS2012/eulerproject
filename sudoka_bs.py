__author__ = 'jianxinsun'

import time



class Sudoka:

    k = 0
    max_depth = 0


    def __init__(self, input):
        self.final_sol = []
        self.pointer_i = []
        self.current_fill = [0]
        for item in input:
            if not item:
                self.max_depth += 1
        self.sol = [input]

        i = 0
        while i<81:
            while i< 81 and self.sol[0][i]:
                i += 1
            self.pointer_i.append(i)
            i += 1

    def solve(self):
        self.backtracking_df()
        print self.final_sol


    def backtracking_df(self):
        if self.solved():
            final_sol = self.sol[self.k]
            return True
        else:
            self.k += 1
            #self.current_fill.append(0)

            sol_set = self.next_sol_prune()

            while not self.final_sol and sol_set:
                self.sol.append(self.sol[self.k-1][:self.pointer_i[self.k-1]] + [sol_set.pop()] + self.sol[self.k-1][self.pointer_i[self.k-1]+1:])
                self.backtracking_df()

            #self.current_fill.pop()
            self.sol.pop()
            self.k -= 1
            #self.current_fill[self.k] = 0

            return self.final_sol


    def solved(self):
        return self.k == self.max_depth


    def next_sol_prune(self):
        pos = self.pointer_i[self.k-1]
        square_row = pos/9/3
        square_column = pos%9/3
        row = [self.sol[self.k-1][pos/9*9+i] for i in range(9)]
        column = [self.sol[self.k-1][pos%9+i*9] for i in range(9)]
        square = [self.sol[self.k-1][square_row*3*9 + square_column*3 + i*9 + j] for i in range(3) for j in range(3)]
        conflict_set = set(row+column+square)
        return [i for i in range(1,10) if not i in conflict_set]


    def compatible(self,candidate):
        pos = self.pointer_i[self.k-1]
        test = self.single_row_compatible(pos,candidate) and self.single_column_compatible(pos,candidate) and self.single_square_compatible(pos,candidate)
        row = [candidate[pos/9*9+i] for i in range(9)]
        column = [candidate[pos%9+i*9] for i in range(9)]
        square_row = pos/9/3
        square_column = pos%9/3
        square = [candidate[square_row*3*9 + square_column*3 + i*9 + j] for i in range(3) for j in range(3)]
        return test


    def single_row_compatible(self,pos,candidate):
        row = [candidate[pos/9*9+i] for i in range(9)]
        return self.check_repeat(row)


    def single_column_compatible(self,pos,candidate):
        column = [candidate[pos%9+i*9] for i in range(9)]
        return self.check_repeat(column)

    def single_square_compatible(self,pos,candidate):
        square_row = pos/9/3
        square_column = pos%9/3
        square = [candidate[square_row*3*9 + square_column*3 + i*9 + j] for i in range(3) for j in range(3)]
        return self.check_repeat(square)

    def check_repeat(self,l):
        count = [0]*len(l)
        for item in l:
            if item:
                count[item-1] += 1
                if count[item-1] > 1:
                    return False
        return True

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
            sudoku_data[sudoku_index] += [int(digit) for digit in line.rstrip('\n')]
    f.close()
    return sudoku_data


def main():
    data = read_sudoku('euler096sudoku.txt')
    sudokas = []
    start = time.time()
    for item in data:
        sudokas.append( Sudoka(item) )
    sudokas[0].solve()
    print time.time() - start


if __name__ == "__main__":
    main()

