from collections import defaultdict

class UnionFind():
    def __init__(self, n: int):
        self.n = n
        self.parents = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    def find(self, x: int):
        if self.parents[x] == -1:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parents[y] = x
        self.siz[x] += self.siz[y]
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        return True

    def same(self, x: int, y: int):
        return self.find(x) == self.find(y)

    def size(self, x: int):
        return self.siz[self.find(x)]

    def all_group_members(self):
        group_members: defaultdict[int, list[int]] = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
