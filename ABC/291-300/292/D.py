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
node_is_seen = [False] * n
path_is_seen = [False] * m

for i in range(m):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    node[u].append((v, i))
    node[v].append((u, i))

for i in range(n):
    if node_is_seen[i]:
        continue
    node_is_seen[i] = True
    node_count = 1
    path_count = 0
    que = deque([i])
    while que:
        now = que.popleft()
        for nx, num in node[now]:
            if path_is_seen[num]:
                continue
            path_is_seen[num] = True
            path_count += 1
            if node_is_seen[nx]:
                continue
            node_is_seen[nx] = True
            node_count += 1
            que.append(nx)
    if node_count != path_count:
        no()
yes()
