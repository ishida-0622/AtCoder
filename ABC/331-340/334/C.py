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
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    if len(lst) % 2 == 0:
        ans = 0
        for i in range(0, len(lst), 2):
            ans += lst[i + 1] - lst[i]
        print(ans)
    else:
        a = []
        for i in range(len(lst) - 1):
            a.append(lst[i + 1] - lst[i])

        even = [0] + list(accumulate([a[i] for i in range(len(a)) if i % 2 == 0]))
        odd = [0] + list(accumulate([a[i] for i in range(len(a)) if i % 2 == 1]))
        sum_a = sum(a)
        ans = sum_a
        for i in range(len(lst)):
            ans = min(ans, sum_a - even[-1] + even[i // 2] - odd[i // 2])
        print(ans)


if __name__ == "__main__":
    main()
