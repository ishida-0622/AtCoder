import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(7*10**5)
import string
import math
from math import gcd, sqrt
from copy import deepcopy
from collections import deque, defaultdict, Counter
from itertools import combinations, permutations, accumulate
from bisect import bisect_left, bisect_right, insort_left, insort_right
from heapq import heapify, heappop, heappush
from functools import lru_cache
from decimal import Decimal, ROUND_HALF_UP
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
def lcm(a,b): return a*b // gcd(a,b)
# Decimal(str(n)).quantize(Decimal("0.1"), ROUND_HALF_UP) <- 四捨五入



class WeightedGraph:
    def __init__(self, n: int):
        self.n = n
        self.node: list[list[tuple[int, int]]] = [[] * n for _ in range(n)]
        self.dist = [float("inf")] * n

    def union(self, x: int, y: int, cost: int, is_directed: bool = False):
        self.node[x].append((y, cost))
        if not is_directed:
            self.node[y].append((x, cost))

    def dijkstra(self, start: int):
        self.dist = [float("inf")] * self.n
        self.dist[start] = 0
        que: list[tuple[int, int]] = []
        for next, c in self.node[start]:
            if c >= 0:
                heappush(que, (c, next))
        while que:
            cost, now = heappop(que)
            if cost > self.dist[now]:
                continue
            self.dist[now] = cost
            for next, c in self.node[now]:
                if c + cost >= self.dist[next]:
                    continue
                heappush(que, (c + cost, next))
        return deepcopy(self.dist)



h, w = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(10)]
g = WeightedGraph(10)

for i in range(10):
    for j in range(10):
        if i != j:
            g.union(i, j, cost[i][j], True)

lst = [list(map(int, input().split())) for _ in range(h)]
_min = [g.dijkstra(i) for i in range(10)]
ans = 0
for i in range(h):
    for j in range(w):
        if lst[i][j] != -1:
            ans += _min[lst[i][j]][1]
print(ans)
