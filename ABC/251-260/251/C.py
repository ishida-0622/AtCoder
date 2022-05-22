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
dic = {}
lst = []
for i in range(n):
    s,t = inputSys().rstrip().split()
    t = int(t)
    lst.append([s,t,s not in dic])
    dic[s] = True

o = False
for i in lst:
    if i[2]:
        o = True
        break

max_point = minf
ans = None
if o:
    for i, v in enumerate(lst):
        if v[2] and v[1] > max_point:
            max_point = v[1]
            ans = i+1
else:
    for i, v in enumerate(lst):
        if v[1] > max_point:
            ans = i+1
print(ans)
