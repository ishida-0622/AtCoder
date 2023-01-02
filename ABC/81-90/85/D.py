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



n, h = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
_max = max(map(lambda x: x[0], lst))
ans = 0
tmp = 0

lst.sort(key=lambda x: x[1], reverse=True)

for i, val in enumerate(lst):
    if val[1] > _max:
        ans += 1
        tmp += val[1]
    if tmp >= h:
        break
    if i >= n-1 or lst[i+1][1] <= _max:
        ans += -(-(h - tmp) // _max)
        break

print(ans)
