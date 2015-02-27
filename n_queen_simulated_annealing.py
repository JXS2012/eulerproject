__author__ = 'jianxin'

import math
import random
import time
import copy
import cProfile

class NQueenMinConflict():
    def __init__(self, n=8, queens=None):
        self.n = n
        if queens is None:
            self.queens = range(1, n+1)
            random.shuffle(self.queens)
        else:
            self.queens = queens
        (self.cost, self.conflicted_queens) = self.cost_function()

    def cost_function(self):
        cost = 0
        conflicted_queens = set()
        for i in range(self.n):
            for j in range(i+1, self.n):
                if (abs(self.queens[j]-self.queens[i]) == j-i) or (self.queens[j] == self.queens[i]):
                    cost += 1
                    conflicted_queens.add(j)
        return cost, conflicted_queens

    def mutate(self):
        q = random.sample(self.conflicted_queens, 1)[0]
        #if random.random() > 1-math.exp((-self.n+len(self.conflicted_queens))/(self.n*1.)):
        if random.random() < 0.9:
            return self.min_conflict_mutate(q)
        else:
            q = random.randint(0, self.n)
            return NQueenMinConflict(self.n, self.queens[:q]+[random.randint(1, self.n+1)]+self.queens[q+1:])

    def min_conflict_mutate(self, q):
        min_conflict = self.cost
        min_conflict_mutate_pos = self.queens[q]
        for i in range(1, self.n+1):
            temp_conflict = 0
            for j in range(self.n):
                if j != q:
                    if (abs(self.queens[j]-i) == abs(j-q)) or (self.queens[j] == i):
                        temp_conflict += 1
            if temp_conflict <= min_conflict:
                min_conflict_mutate_pos = i
                min_conflict = temp_conflict
        min_conflict_queens = self.queens[:]
        min_conflict_queens[q] = min_conflict_mutate_pos
        return NQueenMinConflict(self.n, min_conflict_queens)

    def __str__(self):
        output = ""
        for i in self.queens:
            for k in range(1, len(self.queens)+1):
                if k == i:
                    output += "Q\t"
                else:
                    output += "_\t"
            output += "\n"
        output += "\n"
        return output


class NQueen():
    def __init__(self, n=8, queens=None):
        self.n = n
        if queens is None:
            self.queens = range(1, n+1)
            random.shuffle(self.queens)
        else:
            self.queens = queens
        self.cost = self.cost_function()

    def cost_function(self):
        cost = 0
        for i in range(self.n):
            for j in range(i+1, self.n):
                if math.fabs(self.queens[j]-self.queens[i]) == j-i:
                    cost += 1
        return cost

    def mutate(self):
        (qi, qj) = random.sample(range(self.n), 2)
        new_queen = self.queens[:]
        new_queen[qi] = self.queens[qj]
        new_queen[qj] = self.queens[qi]
        return NQueen(n=self.n, queens=new_queen)

    def __str__(self):
        output = ""
        for i in self.queens:
            for k in range(1, len(self.queens)+1):
                if k == i:
                    output += "Q\t"
                else:
                    output += "_\t"
            output += "\n"
        output += "\n"
        return output


class Particle:
    def __init__(self, value):
        self.value = value
        self.cost = self.cost_function()

    def cost_function(self):
        return self.value.cost

    def mutate(self):
        return Particle(value=self.value.mutate())


class Annealing:
    def __init__(self, value, temperature=1, k=10, iteration_length=500, cooling_rate=0.95):
        self.current_particle = Particle(value)
        self.current_temperature = temperature
        self.k_constant = k
        self.iteration_length = iteration_length
        self.cooling_rate = cooling_rate

    def simulate(self):
        changed = True
        while changed and self.current_particle.cost != 0:
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
                if self.current_particle.cost == 0:
                    break
            print self.current_particle.cost
            self.current_temperature *= self.cooling_rate


def main():
    print "Min Conflict:"
    start = time.time()
    anneal = Annealing(NQueenMinConflict(100))
    anneal.simulate()
    print anneal.current_particle.cost
    print time.time() - start

    print "No heuristic:"
    start = time.time()
    anneal = Annealing(NQueen(100))
    anneal.simulate()
    print anneal.current_particle.cost
    print time.time() - start

if __name__ == "__main__":
    cProfile.run('main()')
