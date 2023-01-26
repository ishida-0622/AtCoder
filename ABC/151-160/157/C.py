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



n, m = map(int, input().split())
C = [None] * 10
f = False
for _ in range(m):
    s, c = map(int, input().split())
    s -= 1
    if C[s] == None:
        C[s] = c
    elif C[s] != c:
        no(-1)

for i in range(1000):
    ok = True
    if len(str(i)) != n:
        continue
    for j, v in enumerate(str(i)):
        if C[j] != int(v) and C[j] != None:
            ok = False
    if ok:
        yes(i)

no(-1)
