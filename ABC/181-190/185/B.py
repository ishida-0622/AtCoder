import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**7)
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



n, m, t = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(m)]
ans = True

now = n - lst[0][0]
if now <= 0:
    ans = False
now = min(n, now + (lst[0][1] - lst[0][0]))

for i in range(1,m):
    a, b = lst[i]
    prev_a, prev_b = lst[i-1]
    now -= (a - prev_b)
    if now <= 0:
        ans = False
    now = min(n, now + (b-a))

if now - (t - lst[-1][1]) <= 0:
    ans = False

YesNo(ans)
