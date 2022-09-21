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



h, w = map(int, inputSys().split())
lst = [list(inputSys().rstrip()) for _ in range(h)]
ls = [[False] * w for _ in range(h)]
i, j = 0, 0
while True:
    if ls[i][j]:
        print(-1)
        exit()
    ls[i][j] = True
    if lst[i][j] == "U":
        if i != 0:
            i -= 1
            continue
        else:
            break
    if lst[i][j] == "D":
        if i != h-1:
            i += 1
            continue
        else:
            break
    if lst[i][j] == "L":
        if j != 0:
            j -= 1
            continue
        else:
            break
    if lst[i][j] == "R":
        if j != w-1:
            j += 1
            continue
        else:
            break
print(i+1, j+1)
