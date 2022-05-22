from collections import deque
import sys
inputSys = sys.stdin.readline
# sys.setrecursionlimit(10**7)
import copy  # copy.deepcopy()
import itertools  # combinations() <- nCr, permutations() <- nPr
import bisect  # 二分探索
import math  # factorial() <- 階乗, sqrt() <- 平方根
from functools import lru_cache # <- メモ化再帰 @lru_cache
import string
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート


q = deque()
Q = int(inputSys())
for i in range(Q):
    s = list(map(int, inputSys().rstrip().split()))
    if s[0] == 1:
        q.append([s[1], s[2]])
    else:
        n = 0
        while True:
            m = q[0]
            if s[1] <= m[1]:
                n += s[1] * m[0]
                q[0][1] -= s[1]
                break
            else:
                n += m[0] * m[1]
                s[1] -= m[1]
                q.popleft()
        print(n)
