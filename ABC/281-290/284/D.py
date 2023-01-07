import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(7*10**5)
import string
import math
from math import gcd, sqrt
from copy import deepcopy
from collections import deque, defaultdict, Counter
from itertools import combinations, permutations, accumulate
from bisect import bisect_left, bisect_right, insort_left, insort_right
from heapq import heapify, heappop, heappush
from functools import lru_cache
from decimal import Decimal, ROUND_HALF_UP
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
def lcm(a,b): return a*b // gcd(a,b)
# Decimal(str(n)).quantize(Decimal("0.1"), ROUND_HALF_UP) <- 四捨五入



def f(N):
    if N % 2 == 0:
        if (N // 2) % 2 == 0:
            return 2, N // 4
        N //= 2
        return math.floor(sqrt(N)), 2
    for i in range(3, N, 2):
        if N % i == 0:
            if (N // i) % i == 0:
                return i, N // (i * i)
            N //= i
            return math.floor(sqrt(N)), i


t = int(input())
for _ in range(t):
    n = int(input())
    print(*f(n))
