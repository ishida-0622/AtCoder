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



n = int(input())
ans = 0

for i in range(1, n):
    a, b = i, n-i
    tmp_a = 0
    tmp_b = 0
    for j in range(1, math.floor(sqrt(a))+1):
        if a % j == 0:
            tmp_a += 2 if j * j != a else 1
    for j in range(1, math.floor(sqrt(b))+1):
        if b % j == 0:
            tmp_b += 2 if j * j != b else 1
    ans += tmp_a * tmp_b
print(ans)
