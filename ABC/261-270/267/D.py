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



n, m = map(int, inputSys().split())
lst = list(map(int, inputSys().split()))

# iまで見てj個選んだ最大値
dp = [[minf]*m for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(min(i,m)):
        if j > 0:
            dp[i][j] = max(dp[i-1][j-1] + lst[i-1] * (j+1), dp[i-1][j])
        else:
            dp[i][j] = max(lst[i-1], dp[i-1][j])

print(dp[-1][-1])
