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



h, w, n, m = map(int, input().split())
ans = 0
light_h = [[-2001, 2001] for _ in range(h)]
light_w = [[-2001, 2001] for _ in range(w)]
block_h = [[-2000, 2000] for _ in range(h)]
block_w = [[-2000, 2000] for _ in range(w)]
light = set()
block = set()

for _ in range(n):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    light_h[a].append(b)
    light_w[b].append(a)
    # insort_left(light_h[a], b)
    # insort_left(light_w[b], a)
    light.add((a, b))
for _ in range(m):
    c, d = map(int, input().split())
    c, d = c-1, d-1
    block_h[c].append(d)
    block_w[d].append(c)
    # insort_left(block_h[c], d)
    # insort_left(block_w[d], c)
    block.add((c, d))

for i in range(h):
    light_h[i].sort()
    block_h[i].sort()
for i in range(w):
    light_w[i].sort()
    block_w[i].sort()

for i in range(h):
    for j in range(w):
        if (i, j) in light:
            ans += 1
            continue
        if (i, j) in block:
            continue
        a = bisect_left(light_h[i], j)
        b = bisect_left(light_w[j], i)
        c = bisect_left(block_h[i], j)
        d = bisect_left(block_w[j], i)
        if light_h[i][a-1] > block_h[i][c-1]:
            ans += 1
            continue
        if light_h[i][a] < block_h[i][c]:
            ans += 1
            continue
        if light_w[j][b-1] > block_w[j][d-1]:
            ans += 1
            continue
        if light_w[j][b] < block_w[j][d]:
            ans += 1
            continue

print(ans)
