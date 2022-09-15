import random
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
lst = list(map(int, inputSys().split()))
ans = 0

ls = sorted([-1 if (v-i)%n==n-1 else (v-i)%n for i, v in enumerate(lst)])

i = 0
m = 0
while ls[i] == -1:
    ls.append(n-1)
    i += 1
    m += 1
while ls[i] == 0:
    ls.append(n)
    i += 1
    m += 1
ls.sort()

i = 0
while i < n+m:
    j = 0
    k = 0
    l = 0
    while i+j < n+m and ls[i] == ls[i+j]:
        j += 1
    while i+j+k < n+m and abs(ls[i] - ls[i+j+k]) <= 1:
        k += 1
    while i+j+k+l < n+m and abs(ls[i] - ls[i+j+k+l]) <= 2:
        l += 1
    i += j
    ans = max(ans, j+k+l)

print(ans)
