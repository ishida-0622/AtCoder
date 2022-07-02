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



n, x = map(int, inputSys().split())
lst = [list(map(int, inputSys().split())) for _ in range(n)]
x -= 1
dp = [inf] * n
sumTime = sum(lst[0])
dp[0] = x * lst[0][1] + sumTime
_min = lst[0][1]

for i in range(1,n):
    sumTime += sum(lst[i])
    _min = min(_min, lst[i][1])
    dp[i] = (x - i) * _min + sumTime

print(min(dp))
