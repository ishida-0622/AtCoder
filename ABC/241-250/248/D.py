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



n = int(input())
lst = list(map(int, inputSys().rstrip().split()))
indexs = [[] for _ in range(n+1)]
for i, val in enumerate(lst):
    indexs[val].append(i)
Q = int(inputSys())

for i in range(Q):
    L, R, X = map(int, inputSys().rstrip().split())
    print(bisect.bisect_right(indexs[X], R-1) - bisect.bisect_left(indexs[X], L-1))
