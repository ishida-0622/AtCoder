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
lst = []
flg = [False] * n

for i in range(n):
    ls = deque(list(map(int, inputSys().split())))
    t, k = ls.popleft(), ls.popleft()
    lst.append([t, k, ls])

que = deque([lst[n-1]])
flg[n-1] = True
ans = 0
while len(que) > 0:
    t, k, ls = que.popleft()
    ans += t
    for i in range(k):
        if not flg[ls[i]-1]:
            que.append(lst[ls[i]-1])
            flg[ls[i]-1] = True

print(ans)
