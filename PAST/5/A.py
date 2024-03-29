import sys

inputSys = sys.stdin.readline
# sys.setrecursionlimit(10**7)
import copy  # copy.deepcopy()
import itertools  # combinations() <- nCr, permutations() <- nPr
import bisect  # 二分探索
import math  # factorial() <- 階乗, sqrt() <- 平方根
from functools import lru_cache  # <- メモ化再帰 @lru_cache
import string

mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")


def YesNo(flag: bool, yes="Yes", no="No"):
    print(yes) if flag else print(no)


# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート


s = input()
o = 0
x = 0
for i in range(5):
    if s[i] == "o":
        o = 0
        while i < 5 and s[i] == "o":
            o += 1
            i += 1
        if o >= 3:
            print("o")
            exit()
    else:
        x = 0
        while i < 5 and s[i] == "x":
            x += 1
            i += 1
        if x >= 3:
            print("x")
            exit()
print("draw")
