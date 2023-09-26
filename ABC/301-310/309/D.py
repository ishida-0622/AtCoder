import math
import string
import sys
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from decimal import ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from heapq import heapify, heappop, heappush
from itertools import accumulate, combinations, groupby, permutations
from math import ceil, cos, floor, gcd, pi, radians, sin, sqrt, tan

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(7 * 10**5)
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
az = string.ascii_lowercase
AZ = string.ascii_uppercase
aZ = string.ascii_letters
zero_nine = string.digits


def YesNo(flag: bool, yes="Yes", no="No"):
    print(yes) if flag else print(no)


def yes(yes="Yes"):
    print(yes)
    exit()


def no(no="No"):
    print(no)
    exit()


def lcm(a: int, b: int):
    return a * b // gcd(a, b)


def round(n: int, d: int = 0):
    return float(Decimal(n).quantize(Decimal(f"1e{d}"), ROUND_HALF_UP))


class Graph:
    def __init__(self, n: int):
        self.n = n
        self.node: list[list[int]] = [[] for _ in range(n)]
        self.is_seen = [False] * n
        self.dists = [0] * n
        self.prev = [-1] * n

    def union(self, x: int, y: int, is_directed: bool = False):
        self.node[x].append(y)
        if not is_directed:
            self.node[y].append(x)

    def bfs(self, start: int):
        self.is_seen = [False] * self.n
        self.is_seen[start] = True
        self.dists = [0] * self.n
        que: deque[tuple[int, int]] = deque([(start, 0)])
        while que:
            now, dist = que.popleft()
            self.dists[now] = dist
            for next in self.node[now]:
                if self.is_seen[next]:
                    continue
                self.is_seen[next] = True
                que.append((next, dist + 1))
        return self.dists

    def bfs_with_root(self, start: int, goal: int):
        self.is_seen = [False] * self.n
        self.prev = [-1] * self.n
        self.is_seen[start] = True
        que: deque[tuple[int, int]] = deque([(start, 0)])
        while que:
            now, dist = que.popleft()
            if now == goal:
                # 経路復元
                root = []
                while now != -1:
                    root.append(now)
                    now = self.prev[now]
                root.reverse()
                return dist, root
            for next in self.node[now]:
                if self.is_seen[next]:
                    continue
                self.is_seen[next] = True
                self.prev[next] = now
                que.append((next, dist + 1))
        return -1, []


def main():
    n1, n2, m = map(int, input().split())
    g1 = Graph(n1)
    g2 = Graph(n2)
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if b <= n1:
            g1.union(a, b)
        else:
            g2.union(a - n1, b - n1)
    res1 = g1.bfs(0)
    res2 = g2.bfs(n2 - 1)
    print(max(res1) + max(res2) + 1)


if __name__ == "__main__":
    main()
