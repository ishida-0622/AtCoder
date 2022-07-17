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



n, k = map(int, inputSys().split())
lst = list(map(int, inputSys().split()))
ans = [-1] * n
cards = []
yama = []

for i in range(n):
    x = lst[i]
    if len(yama) == 0 or yama[-1] < x:
        yama.append(x)
        cards.append([x])
        idx = 0
        if len(cards[idx]) == k:
            yama.pop(idx)
            for val in cards[idx]:
                ans[val-1] = i+1
            cards.pop(idx)
    else:
        idx = bisect.bisect(yama, x)
        yama[idx] = x
        cards[idx].append(x)
        if len(cards[idx]) == k:
            yama.pop(idx)
            for val in cards[idx]:
                ans[val-1] = i+1
            cards.pop(idx)

print(*ans, sep="\n")
