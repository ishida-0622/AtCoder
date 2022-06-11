import sys
inputSys = sys.stdin.readline
# sys.setrecursionlimit(10**7)
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



n, k = map(int, inputSys().split())
a = list(map(int, inputSys().split()))
lst = [list(map(int, inputSys().split())) for _ in range(n)]

ans = 0
for i in range(n):
    if i+1 not in a:
        lst[i].append(False)
    else:
        lst[i].append(True)

for i in range(n):
    if not lst[i][2]:
        m = inf
        for j in range(k):
            m = min(math.sqrt((lst[i][0] - lst[a[j]-1][0]) ** 2 + (lst[i][1] - lst[a[j]-1][1]) ** 2), m)
        ans = max(ans, m)

print(ans)
