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
ans = True
pos = [0, 0]
tt = 0
for i in range(n):
    t, x, y = map(int, inputSys().split())
    if t % 2 != (x + y) % 2 or (abs(x - pos[0]) + abs(y - pos[1])) > t - tt:
        ans = False
    tt = t
    pos = [x, y]
YesNo(ans)
