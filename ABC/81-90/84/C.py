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



n = int(input())
lst = [list(map(int, input().split())) for _ in range(n-1)]
ans = [0] * n

for i in range(n):
    t = 0
    j = 0
    while i+j < n-1:
        if t < lst[i+j][1]:
            t = lst[i+j][1] + lst[i+j][0]
        else:
            t += lst[i+j][2] - ((t - lst[i+j][1]) % lst[i+j][2]) if (t - lst[i+j][1]) % lst[i+j][2] != 0 else 0
            t += lst[i+j][0]
        j += 1
    ans[i] = t
print(*ans, sep="\n")
