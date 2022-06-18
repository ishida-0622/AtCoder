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


def ok():
    res = True
    for i, val in enumerate(lst):
        if sum(val) != H[i]:
            res = False
            break
    if res:
        for i in range(3):
            if lst[0][i] + lst[1][i] + lst[2][i] != W[i]:
                res = False
                break
    return res


lst = list(map(int, inputSys().split()))
H = lst[0:3]
W = lst[3:6]
ans = 0
lst = [[1,1,1] for _ in range(3)]

for i in range(1,30):
    for j in range(1,30):
        for k in range(1,30):
            for l in range(1,30):
                lst[0][0] = i
                lst[0][1] = j
                lst[0][2] = max(1,H[0] - lst[0][0] - lst[0][1])
                lst[1][0] = k
                lst[1][1] = l
                lst[1][2] = max(1,H[1] - lst[1][0] - lst[1][1])
                lst[2][0] = max(1,W[0] - lst[0][0] - lst[1][0])
                lst[2][1] = max(1,W[1] - lst[0][1] - lst[1][1])
                lst[2][2] = max(1,W[2] - lst[0][2] - lst[1][2])
                if ok():
                    ans += 1

print(ans)
