import sys
inputSys = sys.stdin.readline
# sys.setrecursionlimit(10**7)
from copy import deepcopy
from collections import deque
import itertools  # combinations() <- nCr, permutations() <- nPr
import bisect
import math
from functools import lru_cache
import string
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート


def f(ls):
    u, b, l, r = inf, minf, inf, minf
    for i, val in enumerate(ls):
        for j, v in enumerate(val):
            if v == "#":
                u = min(u, i)
                b = max(b, i)
                l = min(l, j)
                r = max(r, j)
    res = [[ls[i][j] for j in range(l, r+1)] for i in range(u, b+1)]
    return res



n = int(inputSys())
s = f([list(inputSys().rstrip()) for _ in range(n)])
t1 = [list(inputSys().rstrip()) for _ in range(n)]
t2 = [[None] * n for _ in range(n)]
t3 = [[None] * n for _ in range(n)]
t4 = [[None] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        tmp = t1[i][j]
        t2[j][n-i-1] = tmp
        t3[n-i-1][n-j-1] = tmp
        t4[n-j-1][i] = tmp

lst = [t1, t2, t3, t4]
ans = False
for i in range(4):
    ls = f(lst[i])
    if ls == s:
        ans = True

YesNo(ans)
