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



a,b,c,d,e,f,x = map(int, inputSys().rstrip().split())
T = 0
A = 0
tmp = x
tmp2 = a
while tmp > 0:
    if tmp2 > 0:
        T += b
        tmp -= 1
        tmp2 -= 1
    else:
        tmp -= c
        tmp2 = a
tmp2 = d
while x > 0:
    if tmp2 > 0:
        A += e
        x -= 1
        tmp2 -= 1
    else:
        x -= f
        tmp2 = d

if T == A:
    print("Draw")
elif T > A:
    print("Takahashi")
else:
    print("Aoki")
