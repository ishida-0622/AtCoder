import sys
inputSys = sys.stdin.readline
# sys.setrecursionlimit(10**7)
import copy  # copy.deepcopy()
import itertools  # combinations() <- nCr, permutations() <- nPr
import bisect  # 二分探索
import math  # factorial() <- 階乗, sqrt() <- 平方根
from functools import lru_cache # <- メモ化再帰 @lru_cache
import string
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート



n, w = map(int, inputSys().rstrip().split())
lst = list(map(int, inputSys().rstrip().split()))
ls = [False] * (w+1)

for i in lst:
    if i <= w:
        ls[i] = True

for i in range(n):
    for j in range(1+i,n):
        if lst[i] + lst[j] <= w:
            ls[lst[i] + lst[j]] = True

for i in range(n):
    for j in range(1+i,n):
        for k in range(1+j,n):
            if lst[i] + lst[j] + lst[k] <= w:
                ls[lst[i] + lst[j] + lst[k]] = True

print(sum(ls))
