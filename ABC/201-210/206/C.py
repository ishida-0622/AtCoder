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
dic = {}
lst = list(map(int, inputSys().split()))
for i, val in enumerate(lst):
    if val not in dic:
        dic[val] = deque([i])
    else:
        dic[val].append(i)
ans = 0
for i, val in enumerate(lst):
    dic[val].popleft()
    ans += n - i - 1 - len(dic[val])
print(ans)
