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


def f(pos, before):
    v[pos] = True
    for val in node[pos]:
        if val == before:
            continue
        if v[val]:
            print("No")
            exit()
        f(val, pos)



n, m = map(int, inputSys().split())
node = [[] for _ in range(n+1)]
v = [False] * (n+1)
cnt = [0] * (n+1)
for i in range(m):
    a, b = map(int, inputSys().split())
    node[a].append(b)
    node[b].append(a)
    cnt[a] += 1
    cnt[b] += 1

ans = max(cnt) < 3

for i, value in enumerate(node):
    for val in value:
        if not v[i]:
            f(val, -1)

YesNo(ans)
