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



def dfs(now):
    for v in edge[now]:
        if node[v]:
            continue
        node[v] = True
        dfs(v)


n = int(input())
edge = {}
node = {}

for _ in range(n):
    a, b = map(int, input().split())
    node[a] = False
    node[b] = False

    if a in edge:
        edge[a].append(b)
    else:
        edge[a] = [b]

    if b in edge:
        edge[b].append(a)
    else:
        edge[b] = [a]

if 1 in edge:
    dfs(1)

ans = 1
for k, v in node.items():
    if v:
        ans = max___(ans, k)

print(ans)
