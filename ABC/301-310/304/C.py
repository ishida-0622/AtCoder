import sys
import string
import math
from math import gcd, sqrt, floor, ceil, radians, sin, cos, tan, pi
from copy import deepcopy
from collections import deque, defaultdict, Counter
from itertools import combinations, permutations, accumulate, groupby
from bisect import bisect_left, bisect_right, insort_left, insort_right
from heapq import heapify, heappop, heappush
from functools import lru_cache, reduce
from decimal import Decimal, ROUND_HALF_UP

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


class UnionFind:
    """Union-Find Tree"""

    def __init__(self, n: int):
        """初期化 Ο(N)

        Args:
            n (int): 頂点数
        """
        self.n = n
        self.parents = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    def union(self, x: int, y: int):
        """頂点xとyを繋ぐ Ο(log N)

        Args:
            x (int): 頂点
            y (int): 頂点

        Returns:
            bool: xとyがすでに同じ集合に属していた場合False, そうでない場合True
        """
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

    def find(self, x: int):
        """頂点xが属する集合の根を返す Ο(log N)

        Args:
            x (int): 頂点

        Returns:
            int: 頂点xが属する集合の根
        """
        if self.parents[x] == -1:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def same(self, x: int, y: int):
        """頂点xとyが同じ集合に属するかを返す Ο(log N)

        Args:
            x (int): 頂点
            y (int): 頂点

        Returns:
            bool: 頂点xとyが同じ集合に属する場合True, そうでない場合False
        """
        return self.find(x) == self.find(y)

    def size(self, x: int):
        """頂点xが所属する集合の要素数を返す Ο(log N)

        Args:
            x (int): 頂点

        Returns:
            int: 頂点xが所属する集合の要素数
        """
        return self.siz[self.find(x)]

    def members(self, x: int):
        """頂点xが属する集合を返す Ο(N log N)

        Args:
            x (int): 頂点

        Returns:
            list[int]: 頂点xが属する集合
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """根の一覧を返す Ο(N)

        Returns:
            list[int]: 根の一覧
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """集合の数を返す Ο(N)

        Returns:
            int: 集合の数
        """
        return len(self.roots())

    def all_group_members(self):
        """全ての集合と属する頂点を返す Ο(N log N)

        Returns:
            defaultdict[int, list[int]]: key: 根, value: その集合に属する頂点
        """
        group_members: defaultdict[int, list[int]] = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        """Ο(N log N)

        Returns:
            str: root: value
        """
        return "\n".join(f"{k}: {v}" for k, v in self.all_group_members().items())


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
    n, d = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            x_1, y_1 = lst[i]
            x_2, y_2 = lst[j]
            if sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) <= d:
                uf.union(i, j)
    for i in range(n):
        YesNo(uf.same(0, i))


if __name__ == "__main__":
    main()
