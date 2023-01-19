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
def yes(yes="Yes"): print(yes);exit()
def no(no="No"): print(no);exit()
def lcm(a,b): return a*b // gcd(a,b)
# Decimal(str(n)).quantize(Decimal("0.1"), ROUND_HALF_UP) <- 四捨五入



s = input()
cnt = [0] * 10
for v in s:
    cnt[int(v)] += 1

if len(s) == 1:
    YesNo(int(s) % 8 == 0)
    exit()
if len(s) == 2:
    if (int(s) % 8 == 0 or int(s[::-1]) % 8 == 0):
        yes()
    no()
for i in range(112, 1000, 8):
    a, b, c = map(int, list(str(i)))
    cnt[a] -= 1
    cnt[b] -= 1
    cnt[c] -= 1
    if cnt[a] >= 0 and cnt[b] >= 0 and cnt[c] >= 0:
        yes()
    cnt[a] += 1
    cnt[b] += 1
    cnt[c] += 1
no()
