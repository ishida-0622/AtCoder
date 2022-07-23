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



L, R, l, r = map(int, inputSys().split())
lst = [[False, False] for _ in range(101)]
for i in range(L, R):
    lst[i][0] = True
for i in range(l, r):
    lst[i][1] = True
ans = 0
for i in range(101):
    if lst[i][0] and lst[i][1]:
        ans += 1
print(ans)
