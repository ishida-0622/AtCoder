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



n = int(input())
color = list(map(int, input().split()))
node = [[] for _ in range(n)]
is_seen = [False] * n
is_seen[0] = True
cnt = [0] * (10 ** 5+1)
ans = []

for _ in range(n-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    node[a].append(b)
    node[b].append(a)

def f(now: int):
    cnt[color[now]] += 1
    if cnt[color[now]] <= 1:
        ans.append(now+1)
    for v in node[now]:
        if is_seen[v]:
            continue
        is_seen[v] = True
        f(v)
    cnt[color[now]] -= 1

f(0)

print(*sorted(ans), sep="\n")
