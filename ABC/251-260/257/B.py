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



n, k, Q = map(int, inputSys().split())
lst = [False] * (n+1)
tmp = list(map(int, inputSys().split()))
for i in tmp:
    lst[i] = True
tmp = list(map(int, inputSys().split()))
for i in range(Q):
    idx = 0
    cnt = 0
    while cnt < tmp[i]:
        if lst[idx]:
            cnt += 1
            if cnt < tmp[i]:
                idx += 1
        else:
            idx += 1
    if idx != n and not lst[idx+1]:
        lst[idx+1] = True
        lst[idx] = False
ans = []
for i, val in enumerate(lst):
    if val:
        ans.append(i)
print(*ans)
