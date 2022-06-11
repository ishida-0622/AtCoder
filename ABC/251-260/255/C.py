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



x, a, d, n = map(int, inputSys().split())
_min = a
_max = d * (n-1) + a
if _min > _max:
    tmp = _min
    _min = _max
    _max = tmp

if x >= _max:
    print(abs(x - _max))
    exit()
elif x <= _min:
    print(abs(x - _min))
    exit()
if d == 0:
    print(abs(x - a))
    exit()

y = min(abs(x - a) % abs(d), abs(d) - abs(x - a) % abs(d))
print(y)
