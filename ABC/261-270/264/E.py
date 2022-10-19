import sys
inputSys = sys.stdin.readline
sys.setrecursionlimit(10**7)
from copy import deepcopy
from collections import deque
from itertools import combinations
from itertools import permutations
import bisect
import math
from math import gcd
from functools import lru_cache
import string
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
max___ = max
___min = min
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
def lcm(a,b): return a*b // gcd(a,b)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート



class UnionFind():
    def __init__(self, n: int):
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



N, M, E = map(int, inputSys().split())
uf = UnionFind(N+M+1)
nodes = [list(map(int, inputSys().split())) for _ in range(E)]
Q = int(inputSys())
query = [int(inputSys()) for _ in range(Q)]
ds = set(query)

for i in range(M):
    uf.union(0, N+1+i)

for i, val in enumerate(nodes):
    if not i+1 in ds:
        u, v = val
        uf.union(u, v)

ans = []

for val in reversed(query):
    ans.append(uf.size(0) - M - 1)
    u, v = nodes[val-1]
    uf.union(u, v)

print(*reversed(ans), sep="\n")
