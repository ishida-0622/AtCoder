import sys
inputSys = sys.stdin.readline
# sys.setrecursionlimit(10**6)
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
s = list(inputSys().rstrip())
for i, val in enumerate(s):
    if val == "A":
        s[i] = "BB"
s = "".join(s)

idx = 0
ln = len(s)
ans = []
while idx < ln:
    if s[idx] == "C":
        ans.append(s[idx])
    else:
        if idx < ln-1 and s[idx+1] == "B":
            ans.append("A")
            idx += 1
        else:
            ans.append("B")
    idx += 1
print(*ans, sep="")
