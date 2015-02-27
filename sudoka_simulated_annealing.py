__author__ = 'jianxin'

import math
import random
import time
import copy


class Sudoku():
    def __init__(self, partial_sol, mutable=None):
        if mutable is None:
            self.mutable = []
            pos = 0
            for i in partial_sol:
                if pos % 9 == 0:
                    self.mutable.append([])
                if i == 0:
                    self.mutable[pos/9].append(pos % 9)
                pos += 1
        else:
            self.mutable = mutable

        self.sudoku = self.fill(partial_sol)
        self.value = self.sudoku[0]*100 + self.sudoku[1]*10 + self.sudoku[2]

    def fill(self, partial_sol):
        filled_sol = []
        for row in range(9):
            row = partial_sol[row*9:row*9+9]
            filled_sol += self.fill_row(row)
        return filled_sol

    def cost(self):
        conflicts = 0
        for row in range(9):
            for column in range(9):
                conflicts += self.single_conflicts(row, column, self.sudoku[row*9+column])
        return conflicts/2

    def single_conflicts(self, row, column, value):
        col_conflict = len([1 for i in [self.sudoku[j*9+column] for j in range(9)] if i == value])-1
        square_row = row/3
        square_column = column/3
        square = [square_row*3*9 + square_column*3 + i*9 + j for i in range(3) for j in range(3)]
        square_conflict = len([1 for i in [self.sudoku[j] for j in square] if i == value])-1
        return col_conflict+square_conflict

    def mutate(self):
        mutable_col = []
        random_row_i = 0
        while len(mutable_col) < 2:
            random_row_i = random.randint(0, 8)
            mutable_col = self.mutable[random_row_i]
        (ci, cj) = random.sample(mutable_col, 2)
        row_i = self.sudoku[random_row_i*9:random_row_i*9+9]
        new_row_i = row_i[:]
        new_row_i[ci] = row_i[cj]
        new_row_i[cj] = row_i[ci]
        return Sudoku(self.sudoku[:random_row_i*9]+new_row_i+self.sudoku[random_row_i*9+9:], self.mutable)

    @staticmethod
    def fill_row(row):
        candidates = [j for j in range(1, 10) if not j in row]
        random.shuffle(candidates)
        filled_row = []
        for i in row:
            if i == 0:
                filled_row.append(candidates.pop())
            else:
                filled_row.append(i)
        return filled_row

    def __str__(self):
        output = ""
        for i in range(9):
            for j in range(9):
                output += "{0}\t".format(self.sudoku[i*9+j])
            output += "\n"
        output += "Conflicts: {0}\n".format(self.cost())
        return output


class Particle:
    def __init__(self, value):
        self.value = value
        self.cost = self.cost_function()

    def cost_function(self):
        return self.value.cost()

    def mutate(self):
        return Particle(self.value.mutate())


class Annealing:
    def __init__(self, value, temperature=10, k=100, iteration_length=100, cooling_rate=0.99):
        self.current_particle = Particle(value)
        self.current_temperature = temperature
        self.k_constant = k
        self.iteration_length = iteration_length
        self.cooling_rate = cooling_rate

    def simulate(self):
        changed = True
        while changed:
            changed = False
            for i in range(self.iteration_length):
                next_particle = self.current_particle.mutate()
                if next_particle.cost <= self.current_particle.cost:
                    self.current_particle = next_particle
                    changed = True
                else:
                    cs = next_particle.cost
                    ci = self.current_particle.cost
                    prob = math.exp(-(cs-ci)/(self.k_constant*self.current_temperature))
                    if prob > random.random():
                        self.current_particle = next_particle
                        changed = True
            self.current_temperature *= self.cooling_rate


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

    sudokus = []
    for puzzle in data:
        sudokus.append(Sudoku(puzzle))
    print "Finished reading"

    start = time.time()
    summation = 0
    for sudoku in sudokus[:1]:
        anneal = Annealing(sudoku)
        anneal.simulate()
        summation += anneal.current_particle.value.value
        print anneal.current_particle.value
    print summation
    print time.time() - start

if __name__ == "__main__":
    main()