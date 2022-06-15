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



n, m, k = map(int, inputSys().split())
dp = [[0] * (k+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(n):
    for j in range(k):
        for l in range(1,m+1):
            if j + l <= k:
                dp[i+1][j+l] = (dp[i+1][j+l] + dp[i][j]) % mod
# print(*dp)
ans = 0
for val in dp[-1]:
    ans = (ans + val) % mod
print(ans)
