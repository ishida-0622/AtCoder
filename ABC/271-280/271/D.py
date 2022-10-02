import sys
inputSys = sys.stdin.readline
sys.setrecursionlimit(10**7)
from copy import deepcopy
from collections import deque
from itertools import combinations
from itertools import permutations
import bisect
import math
from math import gcd
from functools import lru_cache
import string
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
def lcm(a,b): return a*b // gcd(a,b)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート



n, s = map(int, inputSys().split())
dp = [[[False, ""] for _ in range(s+1)] for _ in range(n+1)]
dp[0][0] = [True, ""]

for i in range(n):
    a, b = map(int, inputSys().split())
    for j in range(s+1):
        if dp[i][j][0]:
            if j + a <= s:
                dp[i+1][j+a] = [True, dp[i][j][1] + "H"]
            if j + b <= s:
                dp[i+1][j+b] = [True, dp[i][j][1] + "T"]

if dp[-1][-1][0]:
    print("Yes")
    print(dp[-1][-1][1])
else:
    print("No")
