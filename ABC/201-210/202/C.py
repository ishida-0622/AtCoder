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
A = list(map(int, inputSys().split()))
B = list(map(int, inputSys().split()))
C = list(map(int, inputSys().split()))
# C = list(map(lambda x: x-1, C))
BB = [B[val-1] for val in C]
ans = 0
sA = sorted(A)
sB = sorted(BB)
# sC = sorted(C)
i = 0
j = 0
sA.append(-1)
sB.append(-2)
while i <= n and j <= n:
    if sA[i] == sB[j]:
        cnt = 1
        cnt2 = 1
        while i <= n and sA[i] == sA[i+1]:
            i += 1
            cnt += 1
        while j <= n and sB[j] == sB[j+1]:
            j += 1
            cnt2 += 1
        ans += cnt * cnt2
        i += 1
        j += 1
    elif sA[i] < sB[j]:
        i += 1
    else:
        j += 1
print(ans)
