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


def f(pos):
    v[pos] = True
    for val in node[pos]:
        if not v[val]:
            f(val)



n, m = map(int, inputSys().split())
node = [[] for _ in range(n+1)]
ans = 0
for i in range(m):
    a, b = map(int, inputSys().split())
    node[a].append(b)
v = [False] * (n+1)
for i in range(1,n+1):
    f(i)
    ans += sum(v)
    v = [False] * (n+1)
print(ans)
