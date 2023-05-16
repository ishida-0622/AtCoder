import sys

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(7 * 10**5)
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
    h, w = map(int, input().split())
    A = [list(input()) for _ in range(h)]
    B = [list(input()) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            a = A[i:] + A[:i]
            for k in range(h):
                a[k] = a[k][j:] + a[k][:j]
            if a == B:
                yes()
    no()


if __name__ == "__main__":
    main()
