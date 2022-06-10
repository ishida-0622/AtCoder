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



n = int(inputSys())
lst = []
for i in range(n):
    t, l, r = map(int, inputSys().split())
    if t == 1:
        lst.append([l,r])
    elif t == 2:
        lst.append([l,r-.5])
    elif t == 3:
        lst.append([l+.5,r])
    else:
        lst.append([l+.5,r-.5])
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        l1, r1 = lst[i]
        l2, r2 = lst[j]
        if (l1 <= l2 and r1 >= r2) or (l2 <= l1 and r2 >= r1) or (r1 >= l2 and l1 <= r2) or (l1 <= r2 and l2 <= r1):
            ans += 1

print(ans)
