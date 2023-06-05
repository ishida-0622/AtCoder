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
    n, m, h, k = map(int, input().split())
    s = input()
    items = set([tuple(map(int, input().split())) for _ in range(m)])
    is_consume = {v: False for v in items}
    now = [0, 0]

    for v in s:
        h -= 1
        if h < 0:
            no()
        if v == "R":
            now[0] += 1
        if v == "L":
            now[0] -= 1
        if v == "U":
            now[1] += 1
        if v == "D":
            now[1] -= 1
        t_now = tuple(now)
        if t_now in items:
            if is_consume[t_now]:
                continue
            if h < k:
                is_consume[t_now] = True
                h = k
    yes()


if __name__ == "__main__":
    main()
