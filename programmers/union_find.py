class UnionFind(object):
    def __init__(self, num_of_nodes) -> None:
        self.parents_tab = [i for i in range(1, num_of_nodes + 1)]
        pass

    def find(self, e):
        if self.parents_tab[e] != e:
            self.parents_tab[e] = self.find(self.parents_tab[e])
        return self.parents_tab[e]

    def union(self, a, b):
        a = self.find(a) # get parent of a
        b = self.find(b) # get parent of b
        if a < b:
            self.parents_tab[b] = a
        else:
            self.parents_tab[a] = b