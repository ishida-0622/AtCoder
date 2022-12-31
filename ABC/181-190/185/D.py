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



n, m = map(int, input().split())
if m == 0:
    print(1)
    exit()
if n == m:
    print(0)
    exit()
lst = sorted(list(map(int, input().split())))

if lst[0] != 1:
    lst = [0] + lst
    m += 1
if lst[-1] != n:
    lst += [n+1]
    m += 1
w = inf
ans = 0

for i in range(m-1):
    w = min(w, lst[i+1] - lst[i] - 1) if min(w, lst[i+1] - lst[i] - 1) != 0 else w

for i in range(m-1):
    ans += -(-(lst[i+1] - lst[i] - 1) // w)

print(ans)
