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



n, k = map(int, inputSys().rstrip().split())
A = list(map(int, inputSys().rstrip().split()))
B = list(map(int, inputSys().rstrip().split()))
dp = [[False, False, False] for _ in range(n)]
dp[0] = [True, True, True]

for i in range(n-1):
    if dp[i][1] and abs(A[i] - A[i+1]) <= k:
        dp[i+1][0] = True
        dp[i+1][1] = True
    if dp[i][1] and abs(A[i] - B[i+1]) <= k:
        dp[i+1][0] = True
        dp[i+1][2] = True
    if dp[i][2] and abs(B[i] - A[i+1]) <= k:
        dp[i+1][0] = True
        dp[i+1][1] = True
    if dp[i][2] and abs(B[i] - B[i+1]) <= k:
        dp[i+1][0] = True
        dp[i+1][2] = True

YesNo(dp[-1][0])
