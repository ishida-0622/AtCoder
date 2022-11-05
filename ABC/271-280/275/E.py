import sys
inputSys = sys.stdin.readline
sys.setrecursionlimit(10**7)
import bisect
import string
import math
from math import gcd
from copy import deepcopy
from collections import deque
from collections import defaultdict
from itertools import combinations
from itertools import permutations
from itertools import accumulate
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



N, M, K = map(int, inputSys().split())
dp = [[0]*(N+1) for _ in range(K+1)]
dp[0][0] = 1
inv = pow(M, mod-2, mod)

for i in range(K):
    for j in range(N):
        if dp[i][j] == 0:
            continue
        for k in range(1, M+1):
            if j+k <= N:
                dp[i+1][j+k] += dp[i][j] * inv
                dp[i+1][j+k] %= mod
            else:
                tmp = N - (j+k - N)
                dp[i+1][tmp] += dp[i][j] * inv
                dp[i+1][tmp] %= mod

print(sum([dp[i][-1] for i in range(K+1)]) % mod)