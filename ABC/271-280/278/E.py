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



H, W, N, h, w = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(H)]
# L, R, U, D
dic = {i:[inf, minf, inf, minf] for i in range(1,N+1)}

for i in range(H):
    for j in range(W):
        a = lst[i][j]
        dic[a][0] = ___min(dic[a][0], i)
        dic[a][1] = max___(dic[a][1], i)
        dic[a][2] = ___min(dic[a][2], j)
        dic[a][3] = max___(dic[a][3], j)

for k in range(H-h+1):
    ans = []
    for l in range(W-w+1):
        tmp = 0
        for i in range(1,N+1):
            if dic[i][0] < k or dic[i][1] >= k+h or dic[i][2] < l or dic[i][3] >= l+w:
                tmp += 1
        ans.append(tmp)
    print(*ans)
