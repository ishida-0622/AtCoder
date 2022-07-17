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



n, x, y, z = map(int, inputSys().split())
ma = list(map(int, inputSys().split()))
en = list(map(int, inputSys().split()))
lst = [[ma[i], en[i], ma[i] + en[i], False, n-i] for i in range(n)]
lst.sort(key=lambda x: (x[0], x[4]), reverse=True)
ans = []
for i in range(x):
    lst[i][3] = True
cnt = 0
i = 0
lst.sort(key=lambda x: (x[1], x[4]), reverse=True)
while cnt < y and i < n:
    if lst[i][3]:
        i += 1
    else:
        lst[i][3] = True
        cnt += 1
        i += 1
cnt = 0
i = 0
lst.sort(key=lambda x: (x[2], x[4]), reverse=True)
while cnt < z and i< n:
    if lst[i][3]:
        i += 1
    else:
        lst[i][3] = True
        cnt += 1
        i += 1
lst.sort(key=lambda x: x[4], reverse=True)
for i, val in enumerate(lst):
    if val[3]:
        print(i+1)
