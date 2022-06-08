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



n, k = map(int, inputSys().split())
lst = list(map(int, inputSys().split()))
dic = {}
for val in lst:
    if val not in dic:
        dic[val] = 1
    else:
        dic[val] += 1
sortedDic = sorted(dic.items(), key=lambda x: x[1])
st = set(lst)
if len(st) - k <= 0:
    print(0)
else:
    tmp = len(st) - k
    ans = 0
    for i in range(tmp):
        ans += sortedDic[i][1]
    print(ans)
