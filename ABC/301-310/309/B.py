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


def main():
    n = int(input())
    lst = [list(input()) for _ in range(n)]
    ans = deepcopy(lst)
    for i in range(n - 1):
        ans[0][i + 1] = lst[0][i]
    for i in range(n - 1):
        ans[i + 1][n - 1] = lst[i][n - 1]
    for i in range(n - 1):
        ans[n - 1][n - i - 2] = lst[n - 1][n - i - 1]
    for i in range(n - 1):
        ans[n - i - 2][0] = lst[n - i - 1][0]

    for v in ans:
        print(*v, sep="")


if __name__ == "__main__":
    main()
