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
    k = int(input())
    s = input()
    t = input()
    if abs(len(s) - len(t)) > k:
        no()
    if len(s) == len(t):
        for i in range(len(s)):
            if s[i] != t[i]:
                k -= 1
            if k < 0:
                no()
        yes()
    elif len(s) > len(t):
        if s == t + s[-1] or s == s[0] + t:
            yes()
        for i in range(len(t)):
            if s[i] != t[i]:
                s1 = s[:i] + s[i + 1:]
                t1 = t[:i] + s[i] + t[i:]
                if s == t1 or s1 == t:
                    yes()
                else:
                    no()
    else:
        if t == s + t[-1] or t == t[0] + s:
            yes()
        for i in range(len(s)):
            if s[i] != t[i]:
                s1 = s[:i] + t[i] + s[i:]
                t1 = t[:i] + t[i + 1:]
                if s1 == t or s == t1:
                    yes()
                else:
                    no()


if __name__ == "__main__":
    main()
