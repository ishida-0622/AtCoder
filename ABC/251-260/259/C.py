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



s = inputSys().rstrip()
t = inputSys().rstrip()

s += "A"
t += "A"

i = 0
j = 0
while i < len(s) and j < len(t):
    if s[i] != t[j]:
        if t[j] == s[i-1] and s[i-1] == s[i-2]:
            j += 1
        else:
            print("No")
            exit()
    else:
        i += 1
        j += 1
print("Yes")
