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


def base_n(num_10: int, n: int):
    """10進数 -> n進数変換(n<=36)"""
    if num_10 == 0:
        return "0"
    s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while num_10:
        res += s[num_10 % n]
        num_10 //= n
    return res[::-1]


def main():
    h, w = map(int, input().split())
    lst = [input() for _ in range(h)]
    snuke = "snuke"
    for i in range(h):
        for j in range(w):
            arr: list[tuple[int, int]] = [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
                (1, 1),
                (-1, -1),
                (1, -1),
                (-1, 1),
            ]
            for a, b in arr:
                k = 0
                try:
                    while (
                        0 <= i + a * k < h
                        and 0 <= j + b * k < w
                        and lst[i + a * k][j + b * k] == snuke[k]
                    ):
                        k += 1
                        if k == 5:
                            for l in range(5):
                                print(i + a * l + 1, j + b * l + 1)
                            exit()
                except IndexError as e:
                    pass


if __name__ == "__main__":
    main()
