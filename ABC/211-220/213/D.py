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
    ans.append(pos)
    v[pos] = True
    for val in node[pos]:
        if not v[val]:
            f(val, pos)
    if pos == 1:
        print(*ans)
        exit()
    ans.append(before)



n = int(inputSys())
v = [False] * (n+1)
node = [[] for _ in range(n+1)]
ans = []
for i in range(n-1):
    a, b = map(int, inputSys().split())
    node[a].append(b)
    node[b].append(a)
for i in range(1,n+1):
    node[i].sort()

f(1,1)
print(*ans)
