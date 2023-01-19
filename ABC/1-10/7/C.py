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



h, w = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
sx, sy, gx, gy = sx-1, sy-1, gx-1, gy-1
lst = [list(input()) for _ in range(h)]
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

que = deque([(sx, sy, 0)])
while que:
    x, y, d = que.popleft()
    if x == gx and y == gy:
        print(d)
        exit()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < h and 0 <= ny < w and lst[nx][ny] == ".":
            que.append((nx, ny, d+1))
            lst[nx][ny] = "#"
