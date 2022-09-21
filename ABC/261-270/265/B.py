import sys
inputSys = sys.stdin.readline
sys.setrecursionlimit(10**7)
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



n, m, t = map(int, inputSys().split())
lst = list(map(int, inputSys().split()))
b = [0] * n
for i in range(m):
    x, y = map(int, inputSys().split())
    b[x-1] += y
ans = True
for i in range(n-1):
    t -= lst[i]
    if t <= 0:
        ans = False
        break
    t += b[i+1]
YesNo(ans)
