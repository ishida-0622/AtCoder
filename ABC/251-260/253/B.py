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



h, w = map(int, inputSys().split())
lst = [list(inputSys().rstrip()) for _ in range(h)]
xy = [0,0,0,0]
idx = 0
for i, val in enumerate(lst):
    if "o" in val:
        for j, v in enumerate(val):
            if v == "o":
                xy[idx] = i
                idx += 1
                xy[idx] = j
                idx += 1
print(abs(xy[0] - xy[2]) + abs(xy[1] - xy[3]))
