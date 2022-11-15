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



n, m = map(int, input().split())
node = [[] for _ in range(n+1)]
cnt = [0] * (n+1)
seen = [False] * (n+1)
dist = [0] * (n+1)
cnt[1] = 1
seen[1] = True

for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

que = deque([[1, 0]])
while que:
    now, d = que.popleft()
    for v in node[now]:
        if seen[v]:
            if dist[v] == d + 1:
                cnt[v] += cnt[now]
                cnt[v] %= mod2
            continue
        seen[v] = True
        dist[v] = d+1
        cnt[v] += cnt[now]
        cnt[v] %= mod2
        que.append([v, d+1])

print(cnt[n])
