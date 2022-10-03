import random
import sys
inputSys = sys.stdin.readline
sys.setrecursionlimit(10**7)
from copy import deepcopy
from collections import deque
from itertools import combinations
from itertools import permutations
import bisect
import math
from math import gcd
from functools import lru_cache
import string
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
def lcm(a,b): return a*b // gcd(a,b)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート



n = int(inputSys())
lst = sorted(list(set(map(int, inputSys().split()))))
ans = 0
now = 1
i = 0
tmp = n - len(lst)
m = len(lst)

while i < m:
    if lst[i] == now:
        ans += 1
        i += 1
    else:
        if (m - i) + tmp >= 2:
            ans += 1
            m -= min(2, max(0, 2-tmp))
            tmp = max(0, tmp-2)
        else:
            break
    now += 1
ans += tmp // 2
print(ans)
