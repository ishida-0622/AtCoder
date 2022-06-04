import sys
inputSys = sys.stdin.readline
# sys.setrecursionlimit(10**7)
from copy import deepcopy
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



n, k = map(int, inputSys().split())
lst = list(map(int, inputSys().split()))
sortedLst = sorted(lst)
ans = True

ls = [[] for _ in range(k)]
sLs = [[] for _ in range(k)]
for i in range(n):
    ls[i%k].append(lst[i])
    sLs[i%k].append(sortedLst[i])

for i in range(k):
    if not sorted(ls[i]) == sLs[i]:
        ans = False
        break

YesNo(ans)
