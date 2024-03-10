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


class Graph:
    def __init__(self, n: int):
        self.n = n
        self.node: list[list[int]] = [[] for _ in range(n)]
        self.is_seen = [False] * n
        self.prev = [-1] * n

    def union(self, x: int, y: int, is_directed: bool = False):
        self.node[x].append(y)
        if not is_directed:
            self.node[y].append(x)

    def bfs(self, start: int, goal: int):
        self.is_seen = [False] * self.n
        self.is_seen[start] = True
        que: deque[tuple[int, int]] = deque([(start, 0)])
        while que:
            now, dist = que.popleft()
            if now == goal:
                return dist
            for next in self.node[now]:
                if self.is_seen[next]:
                    continue
                self.is_seen[next] = True
                que.append((next, dist + 1))
        return -1

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


def main():
    n = int(input())
    g = Graph(n)
    for i in range(n):
        lst = list(map(int, input().split()))
        for j in range(n):
            if lst[j] == 1:
                g.union(i, j, True)

    for i in range(n):
        print(*sorted(map(lambda x: x + 1, g.node[i])))


if __name__ == "__main__":
    main()
