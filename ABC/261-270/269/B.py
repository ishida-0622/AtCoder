import sys
inputSys = sys.stdin.readline
sys.setrecursionlimit(10**7)
from copy import deepcopy
from collections import deque
from itertools import combinations
from itertools import permutations
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



lst = [input() for _ in range(10)]

a,b,c,d = 10, 0, 10, 0

for i in range(10):
    for j in range(10):
        if lst[i][j] == "#":
            a = min(a,i+1)
            b = max(b,i+1)
            c = min(c,j+1)
            d = max(d,j+1)

print(a,b)
print(c,d)
