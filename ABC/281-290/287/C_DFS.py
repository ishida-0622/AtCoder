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
is_seen = [False] * n
start = None
goal = None

for _ in range(m):
    u, v = map(int, input().split())
    node[u-1].append(v-1)
    node[v-1].append(u-1)

for i, v in enumerate(node):
    if len(v) > 2:
        no()
    if len(v) == 1:
        if start == None:
            start = i
        elif goal == None:
            goal = i
        else:
            no()

if start == None or goal == None:
    no()

def f(now, before):
    if now == goal:
        return
    for v in node[now]:
        if v == before:
            continue
        if is_seen[v]:
            no()
        is_seen[v] = True
        f(v, now)

is_seen[start] = True
f(start, None)

YesNo(sum(is_seen) == n)
