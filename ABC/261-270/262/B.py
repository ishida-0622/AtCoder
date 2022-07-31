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
e = [[] for _ in range(n+1)]
ans = 0
for i in range(m):
    u, v = map(int, inputSys().split())
    e[u].append(v)
    e[v].append(u)
for i in range(1,n+1):
    for j in range(i+1, n+1):
        for k in range(j+1, n+1):
            if j in e[i] and k in e[j] and i in e[k]:
                ans += 1
print(ans)
