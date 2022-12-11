import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**7)
import bisect
import string
import math
from math import gcd
from copy import deepcopy
from collections import deque, defaultdict
from itertools import combinations, permutations, accumulate
from functools import lru_cache
from decimal import Decimal, ROUND_HALF_UP
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
max___ = max
___min = min
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
def lcm(a,b): return a*b // gcd(a,b)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート
# Decimal(str(n)).quantize(Decimal("0.1"), ROUND_HALF_UP) <- 四捨五入



N, K, D = map(int, input().split())
lst = list(map(int, input().split()))
# i番目まで見てj個選んでmod Dがkになるものの最大値
dp = [[[-1]*D for _ in range(K)] for _ in range(N+1)]

for i in range(N):
    for j in range(min(K, i+1)):
        for k in range(D):
            if j > 0:
                mod_d = (lst[i] + k) % D
                if dp[i][j-1][k] != -1:
                    dp[i+1][j][mod_d] = max([dp[i][j][mod_d], dp[i+1][j][mod_d], dp[i][j-1][k] + lst[i]])
                    continue
                if dp[i][j][mod_d] != -1:
                    dp[i+1][j][mod_d] = max(dp[i+1][j][mod_d], dp[i][j][mod_d])
            else:
                mod_d = lst[i] % D
                dp[i+1][j][mod_d] = max([dp[i][j][mod_d], dp[i+1][j][mod_d], lst[i]])
                if dp[i][j][k] != -1 or j != 0:
                    dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])

print(dp[-1][-1][0])
