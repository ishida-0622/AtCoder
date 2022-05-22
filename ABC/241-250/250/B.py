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



n, a, b = map(int, inputSys().rstrip().split())
lst = [["."] * (n*b) for _ in range(n*a)]

for i in range(n*a):
    for j in range(n*b):
        if (i // a) % 2 == 1 and (j // b) % 2 == 0 or (i // a) % 2 == 0 and (j // b) % 2 == 1:
            lst[i][j] = "#"

for i in lst:
    print(*i, sep="")
