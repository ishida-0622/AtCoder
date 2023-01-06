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



h, w = map(int, input().split())
lst = [input() for _ in range(h)]
is_sean = [[False] * w for _ in range(h)]

is_sean[0][0] = True
que = deque([(0, 0, 0)])
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

while que:
    x, y, dist = que.popleft()
    if x == h-1 and y == w-1:
        print(sum([val.count(".") for val in lst]) - dist - 1)
        exit()
    for a, b in d:
        nx = x + a
        ny = y + b
        if 0 <= nx < h and 0 <= ny < w and not is_sean[nx][ny] and lst[nx][ny] == ".":
            is_sean[nx][ny] = True
            que.append((nx, ny, dist+1))

print(-1)
