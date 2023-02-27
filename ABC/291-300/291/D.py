import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(7*10**5)
import string
import math
from math import gcd, sqrt
from copy import deepcopy
from collections import deque, defaultdict, Counter
from itertools import combinations, permutations, accumulate
from bisect import bisect_left, bisect_right, insort_left, insort_right
from heapq import heapify, heappop, heappush
from functools import lru_cache
from decimal import Decimal, ROUND_HALF_UP
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
def yes(yes="Yes"): print(yes);exit()
def no(no="No"): print(no);exit()
def lcm(a,b): return a*b // gcd(a,b)
# Decimal(str(n)).quantize(Decimal("0.1"), ROUND_HALF_UP) <- 四捨五入



n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[0, 0] for _ in range(n)]
dp[0] = [1, 1]

for i in range(1, n):
    if lst[i-1][0] != lst[i][0]:
        dp[i][0] += dp[i-1][0]
    if lst[i-1][1] != lst[i][0]:
        dp[i][0] += dp[i-1][1]
    if lst[i-1][0] != lst[i][1]:
        dp[i][1] += dp[i-1][0]
    if lst[i-1][1] != lst[i][1]:
        dp[i][1] += dp[i-1][1]
    dp[i][0] %= mod
    dp[i][1] %= mod

print(sum(dp[-1]) % mod)



# def f(l):
#     for i in range(len(l)-1):
#         if l[i] == l[i+1]:
#             return False
#     return True

# ans = 0
# for i in range(2 ** n):
#     ls = []
#     for j in range(n):
#         if i >> j & 1:
#             ls.append(lst[j][1])
#         else:
#             ls.append(lst[j][0])
#     if f(ls):
#         ans += 1
# print(ans)
