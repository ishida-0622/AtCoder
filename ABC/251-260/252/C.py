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


def f(l):
    for i in l:
        if not i[1]:
            return False
    return True


n = int(input())
lst = [input() for _ in range(n)]

ans = [inf] * 10

for i in range(10):
    idx = 0
    ls = [[i, False] for i in lst]
    while (not f(ls)) or idx == 0:
        for j in range(n):
            if (not ls[j][1]) and ls[j][0][idx%10] == str(i):
                ls[j][1] = True
                break
        idx += 1
    ans[i] = idx
print(min(ans)-1)
