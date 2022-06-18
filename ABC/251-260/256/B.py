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
masu = [False] * 4
masu2 = [False] * 4
p = 0
for val in lst:
    masu[0] = True
    for i in range(4):
        if masu[i]:
            if i + val < 4:
                masu2[i + val] = True
            else:
                p += 1
    masu = deepcopy(masu2)
    masu2 = [False] * 4
print(p)
