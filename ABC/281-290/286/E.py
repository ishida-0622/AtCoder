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
def yes(yes="Yes"): print(yes);exit()
def no(no="No"): print(no);exit()
def lcm(a,b): return a*b // gcd(a,b)
# Decimal(str(n)).quantize(Decimal("0.1"), ROUND_HALF_UP) <- 四捨五入



class WarshallFloyd:
    def __init__(self, n: int):
        self.n = n
        self.dist = [[inf] * n for _ in range(n)]
        self.prev = [[-1] * n for _ in range(n)]
        for i in range(n):
            self.dist[i][i] = 0

    def union(self, x: int, y: int, cost: int = 1, is_directed: bool = False):
        self.dist[x][y] = cost
        self.prev[x][y] = x
        if not is_directed:
            self.dist[y][x] = cost
            self.prev[y][x] = y

    def warshall_floyd(self):
        """ワーシャルフロイド法による探索 Ο(N^3)"""
        is_negative = False
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.dist[i][k] + self.dist[k][j] < self.dist[i][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]
                        self.prev[i][j] = self.prev[k][j]
        # 負閉路検出
        for i in range(self.n):
            if self.dist[i][i] < 0:
                is_negative = True
        return self.dist, is_negative

    def get_path(self, start: int, goal: int):
        """
        最短経路の復元. warshall_floydが実行されているのが前提
        """
        path = []
        now = goal
        while now != start:
            path.append(now)
            now = self.prev[start][now]
            if now == -1:
                return -1
        path.append(start)
        path.reverse()
        return path



n = int(input())
A = list(map(int, input().split()))
g = WarshallFloyd(n)

for i in range(n):
    s = input()
    for j, v in enumerate(s):
        if v == "Y":
            g.union(i, j, 10 ** 10 - A[j], True)

g.warshall_floyd()
Q = int(input())

for _ in range(Q):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    p = g.get_path(u, v)
    if p == -1:
        print("Impossible")
    else:
        print(len(p)-1, sum([A[v] for v in p]))
