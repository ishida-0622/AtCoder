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
node = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    node[u].append(v)

ans = 0

for i in range(n):
    que = deque([[i, 0]])
    count = 0
    is_seen = [False] * n
    is_seen[i] = True
    while que:
        now, dist = que.popleft()
        if dist > 1:
            count += 1
        for nx in node[now]:
            if is_seen[nx]:
                continue
            is_seen[nx] = True
            que.append([nx, dist+1])
    ans += count

print(ans)
