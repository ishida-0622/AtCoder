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



n,k,x = map(int, inputSys().rstrip().split())
lst = list(map(int, inputSys().rstrip().split()))

for i in range(n):
    while lst[i] >= x and k > 0:
        tmp = k*1
        k -= min(lst[i] // x, k)
        lst[i] -= min(x * (lst[i] // x), x * tmp)

if k > 0:
    lst.sort(reverse=True)
    i = 0
    while k > 0 and i < n:
        lst[i] = 0
        i += 1
        k -= 1
print(sum(lst))
