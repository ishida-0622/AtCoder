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



n, m, Q = map(int, input().split())
V = [list(map(int, input().split())) for _ in range(n)]
X = list(map(int, input().split()))
V.sort(key=lambda x:x[1], reverse=True)

for _ in range(Q):
    l, r = map(int, input().split())
    x = sorted(X[:l-1] + X[r:])
    f = [False] * n
    ans = 0
    for xx in x:
        for i, wv in enumerate(V):
            w, v = wv
            if xx >= w and not f[i]:
                ans += v
                f[i] = True
                break
    print(ans)
