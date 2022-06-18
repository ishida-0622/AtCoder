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
LR = [list(map(int, inputSys().split())) for _ in range(n)]
LR.sort()
ans = []
i = 0
while i < n:
    L, R = LR[i]
    j = 1
    while i+j < n and LR[i+j][0] <= R:
        R = max(R ,LR[i+j][1])
        j += 1
    ans.append([L,R])
    i += j

ans.sort()
for val in ans:
    print(*val)
