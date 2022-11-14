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


# 時刻iに座標jにいる場合の最大値
# その場にとどまる or 隣に移動する
n = int(inputSys())
sunuke = [[0] * 5 for _ in range(10 ** 5)]
dp = [[0] * 5 for _ in range(10 ** 5)]

for i in range(n):
    t, x, a = map(int, inputSys().split())
    sunuke[t-1][x] += a

for i in range(10**5):
    if i == 0:
        pass
    for j in range(min(5, i+1)):
        if j == 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + sunuke[i][j])
            dp[i][j+1] = max(dp[i][j+1], dp[i-1][j] + sunuke[i][j+1])
            continue
        if j == 4:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + sunuke[i][j])
            dp[i][j-1] = max(dp[i][j-1], dp[i-1][j] + sunuke[i][j-1])
            continue
        dp[i][j] = max(dp[i][j], dp[i-1][j] + sunuke[i][j])
        dp[i][j+1] = max(dp[i][j+1], dp[i-1][j] + sunuke[i][j+1])
        dp[i][j-1] = max(dp[i][j-1], dp[i-1][j] + sunuke[i][j-1])

print(max(dp[-1]))
