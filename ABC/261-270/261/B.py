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
ans = True
for i in range(n):
    for j in range(n):
        if lst[i][j] == "-":
            continue
        if lst[i][j] == "W" and lst[j][i] != "L":
            ans = False
        if lst[i][j] == "L" and lst[j][i] != "W":
            ans = False
        if lst[i][j] == "D" and lst[j][i] != "D":
            ans = False

YesNo(ans, "correct", "incorrect")
