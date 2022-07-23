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
X = list(map(int, inputSys().split()))
Y = [0] * (n+1)
for i in range(m):
    c, y = map(int, inputSys().split())
    Y[c] = y

# i回目のトスでカウントがjになる場合の最大金額
dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(i+1):
        # 表
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + X[i] + Y[j+1])
        # 裏
        dp[i+1][0] = max(dp[i+1][0], dp[i][j])

print(max(dp[-1]))
