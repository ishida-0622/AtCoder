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



n = int(inputSys())
lst = [inputSys().rstrip().split() for _ in range(n)]
ans = True
for i, val in enumerate(lst):
    a = val[0]
    b = val[1]
    af = False
    bf = False
    for j in range(n):
        if lst[j][0] == a or lst[j][1] == a:
            if j != i:
                af = True
        if lst[j][0] == b or lst[j][1] == b:
            if j != i:
                bf = True
    if af and bf:
        ans = False
YesNo(ans)
