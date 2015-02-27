__author__ = 'jianxinsun'


import operator
import copy
import time


class ConsistencyGraphNode():
    def __init__(self, value=0, pos=0, n=8):
        if value != 0:
            self.current_value = value
            self.to_explore_value = {value}
        else:
            self.current_value = 0
            self.to_explore_value = set(range(1, n+1))

        self.price = len(self.to_explore_value)
        self.pos = pos

    def set_value(self, value):
        self.price = 1
        self.current_value = value
        self.to_explore_value = {value}

    def remove_conflict(self, conflict):

        self.to_explore_value -= {conflict.current_value,
                                  abs(self.pos-conflict.pos)+conflict.current_value,
                                  -abs(self.pos-conflict.pos)+conflict.current_value}
                                  #-self.pos+conflict.pos+conflict.current_value,
                                  #-self.pos+conflict.pos-conflict.current_value}
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

    def __init__(self, n=8):
        self.graph = {}
        nodes = [ConsistencyGraphNode(pos=k, n=n) for k in range(1, n+1)]

        for item in nodes:
            linked_nodes = nodes[:]
            linked_nodes.remove(item)
            self.graph[item] = linked_nodes

        self.updated = True
        self.recursive_forward_checking()

    def next_assignments(self):
        reduced_key_set = [key for key in self.graph.keys() if key.price != 1]
        most_constrained = min(reduced_key_set, key=operator.attrgetter('price'))
        if most_constrained.price == 0:
            return []
        else:
            next_assignments = []

            most_constrained_nodes = [node for node in self.graph.keys() if node.price == most_constrained.price]
            if len(most_constrained_nodes) != 1:
                most_constrained = self.most_constraining(most_constrained_nodes)

            ranked_value_set = self.least_constraining_value(most_constrained)

            for node_value, unused in ranked_value_set:
                new_graph = copy.deepcopy(self)
                key = next(i for i in new_graph.graph.keys() if i.pos == most_constrained.pos)
                key.set_value(node_value)
                next_assignments.append(new_graph)

            return next_assignments

    def least_constraining_value(self, node):
        ranked_value = []

        for value in node.to_explore_value:
            value_removed = len([i for i in self.graph[node] if value in i.to_explore_value])
            ranked_value.append((value, value_removed))

        ranked_value = sorted(ranked_value, key=operator.itemgetter(1))

        return ranked_value

    def most_constraining(self, nodes):
        max_constraints = 0
        most_constraining = nodes[0]
        for node in nodes:
            constraints = len([i for i in self.graph[node] if i.price != 1])
            if constraints > max_constraints:
                most_constraining = node
                max_constraints = constraints
        return most_constraining

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
                    if linked_node.remove_conflict(key):
                        self.updated = True

    def __str__(self):
        output = ""
        key_set = sorted(self.graph.keys(), key=operator.attrgetter('pos'))
        for i in key_set:
            for k in range(1,len(key_set)+1):
                if k == i.current_value:
                    output += "Q\t"
                else:
                    output += "_\t"
            output += "\n"
        output += "\n"
        return output

    def solved(self):
        min_key = min(self.graph.keys(), key=operator.attrgetter('price'))
        max_key = max(self.graph.keys(), key=operator.attrgetter('price'))
        return min_key.price == 1 and max_key.price == 1


class SearchTreeNode:

    def __init__(self, value=None, parent=None, n=8):
        if value is None:
            self.value = ConsistencyGraph(n)
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

    def __init__(self, k):
        self.root = SearchTreeNode(n=k)
        self.current_node = self.root
        self.solved = False
        self.value = 0

    def add(self):
        self.current_node.add_leaf()

    def df_search(self):
        self.current_node.value.recursive_forward_checking()

        if self.current_node.solved():
            print "solved"
            print self.current_node.value
            self.solved = True
            self.value += 1
            return
        else:
            #print "expand to"
            #print self.current_node.value
            self.add()

            for leaf in self.current_node.children:
                self.current_node = leaf
                self.df_search()
                if self.solved:
                    break
                self.current_node = leaf.parent
                #print "back up to"
                #print self.current_node.value

            return


def main():
    eight_queen = SearchTree(100)
    start = time.time()
    eight_queen.df_search()
    print eight_queen.value
    print time.time() - start


if __name__ == "__main__":
    main()