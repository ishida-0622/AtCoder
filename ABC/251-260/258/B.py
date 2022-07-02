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



n = int(inputSys())
lst = [list(inputSys().rstrip()) for _ in range(n)]
ans = -1
for i in range(n):
    for j in range(n):
        tmp = lst[i][j]
        for k in range(1,n):
            tmp += lst[(i+k)%n][j]
        ans = max(ans, int(tmp))

        tmp = lst[i][j]
        for k in range(1, n):
            tmp += lst[(n+i-k)%n][j]
        ans = max(ans, int(tmp))

        tmp = lst[i][j]
        for k in range(1, n):
            tmp += lst[i][(j+k)%n]
        ans = max(ans, int(tmp))

        tmp = lst[i][j]
        for k in range(1,n):
            tmp += lst[i][(n+j-k)%n]
        ans = max(ans, int(tmp))

        tmp = lst[i][j]
        for k in range(1,n):
            tmp += lst[(i+k)%n][(j+k)%n]
        ans = max(ans, int(tmp))

        tmp = lst[i][j]
        for k in range(1,n):
            tmp += lst[(n+i-k)%n][(n+j-k)%n]
        ans = max(ans, int(tmp))

        tmp = lst[i][j]
        for k in range(1,n):
            tmp += lst[(i+k)%n][(n+j-k)%n]
        ans = max(ans, int(tmp))

        tmp = lst[i][j]
        for k in range(1,n):
            tmp += lst[(n+i-k)%n][(j+k)%n]
        ans = max(ans, int(tmp))
print(ans)
