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
lst2 = [1 if i+1 == v else 0 for i, v in enumerate(lst)]
_sum = sum(lst2)-1
for i in range(n):
    if lst2[i]:
        lst2[i] = _sum
        _sum -= 1
ans = 0

for i in range(n):
    if lst[i] == i+1:
        ans += lst2[i]
    else:
        if lst[lst[i]-1] == i+1 and i < lst[i]:
            ans += 1

print(ans)
