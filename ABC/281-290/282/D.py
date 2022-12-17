import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**7)
import bisect
import string
import math
from math import gcd
from copy import deepcopy
from collections import deque, defaultdict
from itertools import combinations, permutations, accumulate
from functools import lru_cache
from decimal import Decimal, ROUND_HALF_UP
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
# Decimal(str(n)).quantize(Decimal("0.1"), ROUND_HALF_UP) <- 四捨五入



class UnionFind():
    def __init__(self, n: int):
        self.parents = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n
        self.n = n

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
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members



def f(now: int, color: int):
    for v in node[now]:
        if node_color[v] == None:
            node_color[v] = (color+1) % 2
            f(v, (color+1) % 2)
        elif node_color[v] == node_color[now]:
            print(0)
            exit()

n, m = map(int, input().split())
node = [[] for _ in range(n+1)]
node_color = [None] * (n+1)
uf = UnionFind(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)
    uf.union(a, b)

for i in range(1,n+1):
    if node_color[i] == None:
        f(i, 0)

ans = n * (n-1) // 2

for key, val in uf.all_group_members().items():
    if key == 0:
        continue
    black = 0
    white = 0
    for v in val:
        if node_color[v] == 0:
            black += 1
        else:
            white += 1
    ans -= black * (black-1) // 2
    ans -= white * (white-1) // 2

ans -= m
print(ans)
