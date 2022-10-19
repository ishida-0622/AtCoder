import sys
inputSys = sys.stdin.readline
sys.setrecursionlimit(10**7)
from copy import deepcopy
from collections import deque
from collections import defaultdict
from itertools import combinations
from itertools import permutations
from itertools import accumulate
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


N, M = map(int, inputSys().split())
uf = UnionFind(N+1)
cnt = [0] * (N+1)
ans = True

for _ in range(M):
    a, b = map(int, inputSys().split())
    cnt[a] += 1
    cnt[b] += 1
    if uf.same(a, b):
        ans = False
    uf.union(a, b)

YesNo(ans and max(cnt) <= 2)
