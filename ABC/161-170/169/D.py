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
p = []
d = defaultdict(int)

while n % 2 == 0:
    p.append(2)
    d[2] += 1
    n //= 2

for i in range(3, math.floor(sqrt(n))):
    while n % i == 0:
        p.append(i)
        d[i] += 1
        n //= i

if n != 1:
    p.append(n)
    d[n] += 1

ans = 0

for v in d.values():
    i = 1
    while v >= i:
        ans += 1
        v -= i
        i += 1

print(ans)
