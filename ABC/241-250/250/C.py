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



n, Q = map(int, inputSys().split())
lst = [i+1 for i in range(n)]
pos = {}
for i, val in enumerate(lst):
    pos[val] = i
for i in range(Q):
    x = int(inputSys())
    idx = pos[x]
    tmp = lst[idx]
    if idx != n-1:
        lst[idx] = lst[idx+1]
        lst[idx+1] = tmp
        y = lst[idx]
        pos[x] = idx+1
        pos[y] = idx
    else:
        lst[idx] = lst[idx-1]
        lst[idx-1] = tmp
        y = lst[idx]
        pos[x] = idx-1
        pos[y] = idx

print(*lst)
