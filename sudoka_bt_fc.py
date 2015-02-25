__author__ = 'jianxinsun'


import operator
import copy
import time


class ConsistencyGraphNode():
    def __init__(self, value=0, pos=0):
        if value != 0:
            self.current_value = value
            self.to_explore_value = {value}
        else:
            self.current_value = 0
            self.to_explore_value = set(range(1, 10))

        self.price = len(self.to_explore_value)
        self.pos = pos

    def set_value(self, value):
        self.price = 1
        self.current_value = value
        self.to_explore_value = {value}

    def remove_conflict(self, conflict):
        self.to_explore_value -= {conflict}
        if self.price > len(self.to_explore_value):
            self.price = len(self.to_explore_value)
            if self.price == 1:
                self.current_value = next(iter(self.to_explore_value))
            return True
        else:
            return False

    def __str__(self):
        return "{0}".format(self.current_value)


class ConsistencyGraph():
    max_k = 1

    def __init__(self, sudoka_raw=None):
        self.graph = {}
        nodes = []

        pos = 0
        for item in sudoka_raw:
            nodes.append(ConsistencyGraphNode(item, pos))
            pos += 1

        pos = 0
        for item in nodes:
            square_row = pos/9/3
            square_column = pos % 9/3
            row = [pos/9*9+i for i in range(9)]
            column = [pos % 9+i*9 for i in range(9)]
            square = [square_row*3*9 + square_column*3 + i*9 + j for i in range(3) for j in range(3)]
            arcs = set(row+column+square) - {pos}

            linked_nodes = []
            for arc in arcs:
                linked_nodes.append(nodes[arc])

            self.graph[item] = linked_nodes

            pos += 1
        self.updated = True
        self.recursive_forward_checking()

    def next_assignments(self):
        reduced_key_set = [key for key in self.graph.keys() if key.price != 1]
        least_choice = min(reduced_key_set, key=operator.attrgetter('price'))
        if least_choice.price == 0:
            return []
        else:
            next_assignments = []
            for node_value in least_choice.to_explore_value:
                new_graph = copy.deepcopy(self)
                key = next(i for i in new_graph.graph.keys() if i.pos == least_choice.pos)
                key.set_value(node_value)
                next_assignments.append(new_graph)

            return next_assignments

    def recursive_forward_checking(self):
        level = 0
        self.updated = True
        while self.updated:
            self.forward_checking()
            level += 1

    def forward_checking(self):
        self.updated = False
        for key in self.graph.keys():
            if key.current_value != 0:
                for linked_node in self.graph[key]:
                    if linked_node.remove_conflict(key.current_value):
                        self.updated = True

    def __str__(self):
        output = ""
        key_set = sorted(self.graph.keys(), key=operator.attrgetter('pos'))
        for i in range(9):
            for j in range(9):
                output += "{0}\t".format(key_set[i*9+j])
            output += "\n"

        singleton = 0
        for key in key_set:
            if key.price == 1:
                singleton += 1
            #output += "{0}\n".format(key.to_explore_value)
        output += "Singleton: {0}\n".format(singleton)
        return output

    def solved(self):
        max_key = max(self.graph.keys(), key=operator.attrgetter('price'))
        min_key = min(self.graph.keys(), key=operator.attrgetter('price'))
        return max_key.price == 1 and min_key.price == 1


class SearchTreeNode:

    def __init__(self, sudoka_raw=None, value=None, parent=None):
        if sudoka_raw is not None:
            self.value = ConsistencyGraph(sudoka_raw)
            self.children = []
            self.parent = None
        else:
            self.value = value
            self.children = []
            self.parent = parent

    def add_leaf(self):
        leaf_graphs = self.value.next_assignments()
        for leaf_graph in leaf_graphs:
            self.children.append(SearchTreeNode(value=leaf_graph, parent=self))

    def solved(self):
        return self.value.solved()


class SearchTree:

    def __init__(self, sudoka_raw):
        self.root = SearchTreeNode(sudoka_raw)
        self.current_node = self.root
        self.solved = False
        self.value = 0

    def add(self):
        self.current_node.add_leaf()

    def df_search(self):
        self.current_node.value.recursive_forward_checking()

        if self.current_node.solved():
            print "solved"
            #print self.current_node.value
            self.solved = True
            key_set = sorted(self.current_node.value.graph.keys(), key=operator.attrgetter('pos'))
            self.value = key_set[0].current_value*100 + key_set[1].current_value*10 + key_set[2].current_value
            print self.value
            return
        else:
            self.add()
            #print "expand to"
            #print self.current_node.value

            for leaf in self.current_node.children:
                self.current_node = leaf
                self.df_search()
                if self.solved:
                    break
                self.current_node = leaf.parent
                #print "back up to"
                #print self.current_node.value

            return


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
    sudoka_forest = []
    for puzzle in data:
        sudoka_forest.append(SearchTree(puzzle))
    print "Finished reading"
    start = time.time()
    summation = 0
    for sudoka_tree in sudoka_forest:
        sudoka_tree.df_search()
        summation += sudoka_tree.value
    print summation
    print time.time() - start

if __name__ == "__main__":
    main()