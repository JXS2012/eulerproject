__author__ = 'jianxin'

import math
import random
import time
import copy
import cProfile


class NQueenMinConflict():
    def __init__(self, n=8, queens=None, cost=None, q_attacked_by=None, conflicted_queens=None):
        self.n = n
        if queens is None:
            self.queens = range(1, n+1)
            random.shuffle(self.queens)
            (self.cost, self.conflicted_queens, self.q_attacked_by) = self.cost_function()
        else:
            self.queens = queens
            self.cost = cost
            self.q_attacked_by = q_attacked_by
            self.conflicted_queens = conflicted_queens

    def cost_function(self):
        conflicted_queens = []
        q_attacked_by = []
        for i in range(self.n):
            q_attacked = 0
            q_conflict = []
            for j in range(i+1, self.n):
                diff = self.queens[j]-self.queens[i]
                if (diff == 0) or (diff == j-i) or (diff == i-j):
                    q_attacked += 1
                    q_conflict.append(j)
            conflicted_queens.append(q_conflict)
            q_attacked_by.append(q_attacked)
        return sum(q_attacked_by), conflicted_queens, q_attacked_by

    def mutate(self):
        conflicted_queens_set = self.get_conflict_set()
        q = random.sample(conflicted_queens_set, 1)[0]
        #print "from {0} mutate {1}".format(conflicted_queens_set, q)
        #print self.cost
        min_mutate = self.min_conflict_mutate(q)
        if min_mutate.get_conflict_set() - conflicted_queens_set or min_mutate.cost != self.cost:
            return min_mutate
        else:
            new_queens = self.queens[:q]+[random.randint(1, self.n)]+self.queens[q+1:]
            (cost, conflicted_queens, q_attacked_by) = self.update_cost(q, new_queens)
            return NQueenMinConflict(self.n, new_queens, cost, q_attacked_by, conflicted_queens)

    def get_conflict_set(self):
        conflicted_queens_total = []
        pos = 0
        for i in self.conflicted_queens:
            conflicted_queens_total += i
            if i:
                conflicted_queens_total += [pos]
            pos += 1
        return set(conflicted_queens_total)

    def min_conflict_mutate(self, q):
        min_conflict = self.cost
        min_conflict_mutate_pos = self.queens[q]
        
        for i in range(1, self.n+1):
            temp_conflict = 0
            for j in range(self.n):
                if j != q:
                    if self.queens[j]-i == j-q or self.queens[j]-i == q-j or self.queens[j] == i:
                        temp_conflict += 1
            if temp_conflict <= min_conflict:
                min_conflict_mutate_pos = i
                min_conflict = temp_conflict
            if temp_conflict == 0:
                break
                
        min_conflict_queens = self.queens[:]
        min_conflict_queens[q] = min_conflict_mutate_pos
        (cost, conflicted_queens, q_attacked_by) = self.update_cost(q, min_conflict_queens)
        return NQueenMinConflict(self.n, min_conflict_queens, cost, q_attacked_by, conflicted_queens)

    def update_cost(self, q, new_queens):
        q_attacked_by = self.q_attacked_by[:]
        conflicted_queens = copy.deepcopy(self.conflicted_queens)

        q_attacked_by[q] = 0
        conflicted_queens[q] = []
        for j in range(q+1, self.n):
            diff = new_queens[q]-new_queens[j]
            if diff == 0 or diff == q-j or diff == j-q:
                q_attacked_by[q] += 1
                conflicted_queens[q].append(j)

        for j in range(q):
            diff = new_queens[q] - new_queens[j]
            diff_ori = self.queens[q] - self.queens[j]
            if diff == -diff_ori:
                pass
            else:
                if diff == q-j or diff == j-q or diff == 0:
                    q_attacked_by[j] += 1
                    conflicted_queens[j].append(q)
                else:
                    if diff_ori == q-j or diff_ori == j-q or diff == 0:
                        q_attacked_by[j] -= 1
                        conflicted_queens[j].remove(q)

        return sum(q_attacked_by), conflicted_queens, q_attacked_by

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
    def __init__(self, n=8, queens=None, q_attacked_by=None):
        self.n = n
        if queens is None:
            self.queens = range(1, n+1)
            random.shuffle(self.queens)
        else:
            self.queens = queens
        if q_attacked_by is None:
            self.q_attacked_by, self.cost = self.cost_function()
        else:
            self.q_attacked_by = q_attacked_by
            self.cost = sum(q_attacked_by)

    def cost_function(self):
        q_attacked_by = []
        for i in range(self.n):
            q_cost = 0
            for j in range(i+1, self.n):
                diff = self.queens[j]-self.queens[i]
                if (diff == j-i) or (diff == i-j):
                    q_cost += 1
            q_attacked_by.append(q_cost)
        return q_attacked_by, sum(q_attacked_by)

    def mutate(self):
        (qi, qj) = random.sample(range(self.n), 2)
        if qi > qj:
            temp = qi
            qi = qj
            qj = temp

        new_queen = self.queens[:]
        new_queen[qi] = self.queens[qj]
        new_queen[qj] = self.queens[qi]

        new_q_attacked_by = self.q_attacked_by[:]
        new_q_attacked_by[qi] = 0
        new_q_attacked_by[qj] = 0

        for j in range(qi+1, self.n):
            diff = new_queen[j] - new_queen[qi]
            if (diff == j-qi) or (diff == qi-j):
                new_q_attacked_by[qi] += 1

        for j in range(qj+1, self.n):
            diff = new_queen[j] - new_queen[qj]
            if (diff == j-qj) or (diff == qj-j):
                new_q_attacked_by[qj] += 1

        for j in range(qi):
            self.update_cost_q(new_queen[j] - new_queen[qi], self.queens[j] - self.queens[qi], qi, j, new_q_attacked_by)
            self.update_cost_q(new_queen[j] - new_queen[qj], self.queens[j] - self.queens[qj], qj, j, new_q_attacked_by)

        for j in range(qi+1, qj):
            self.update_cost_q(new_queen[j] - new_queen[qj], self.queens[j] - self.queens[qj], qj, j, new_q_attacked_by)

        return NQueen(n=self.n, queens=new_queen, q_attacked_by=new_q_attacked_by)

    @staticmethod
    def update_cost_q(diff_i, diff_i_ori, i, j, q_attack):
        if diff_i == - diff_i_ori:
            pass
        else:
            if diff_i == j-i or diff_i == i-j:
                q_attack[j] += 1
            else:
                if diff_i_ori == j-i or diff_i_ori == i-j:
                    q_attack[j] -= 1


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
    anneal = Annealing(NQueenMinConflict(10))
    anneal.simulate()
    print anneal.current_particle.cost
    #print anneal.current_particle.value
    print time.time() - start

    print "No heuristic:"
    anneal = Annealing(NQueen(10))
    anneal.simulate()
    #print anneal.current_particle.value
    print anneal.current_particle.cost

if __name__ == "__main__":
    cProfile.run('main()')