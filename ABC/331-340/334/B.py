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
    A, M, L, R = map(int, input().split())
    L -= A
    R -= A
    l = abs(L) // M
    if L < 0:
        l *= -1
    r = abs(R) // M
    if R < 0:
        r *= -1
    print(
        abs(r - l)
        + (0 if (0 < L <= R or L <= R < 0) else 1)
        + int(L > 0 and L % M == 0)
        + int(R < 0 and R % M == 0)
    )


if __name__ == "__main__":
    main()
