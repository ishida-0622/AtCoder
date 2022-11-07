import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**7)
import bisect
import string
import math
from math import gcd
from copy import deepcopy
from collections import deque, defaultdict
from itertools import combinations, permutations, accumulate
from functools import lru_cache
from decimal import Decimal, ROUND_HALF_UP
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
max___ = max
___min = min
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
def lcm(a,b): return a*b // gcd(a,b)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート
# Decimal(str(n)).quantize(Decimal("0.1"), ROUND_HALF_UP) <- 四捨五入



def bfs(sx, sy, gx, gy):
    if not 0 <= sx < h or not 0 <= sy < w or C[sx][sy] == "#":
        return False
    lst = deepcopy(C)
    lst[sx][sy] = "#"
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    que = deque([[sx, sy]])
    while que:
        x, y = que.popleft()
        if x == gx and y == gy:
            return True
        for a, b in zip(dx, dy):
            nx, ny = x+a, y+b
            if 0 <= nx < h and 0 <= ny < w and lst[nx][ny] == ".":
                que.append([nx, ny])
                lst[nx][ny] = "#"
    return False


h, w = map(int, input().split())
C = [list(input()) for _ in range(h)]
sx, xy = 0, 0
ans = False

for i, val in enumerate(C):
    for j, v in enumerate(val):
        if v == "S":
            sx, sy = i, j

d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for s, g in combinations(d, 2):
    a, b = s
    aa, bb = g
    if bfs(sx+a, sy+b, sx+aa, sy+bb):
        ans = True

YesNo(ans)
