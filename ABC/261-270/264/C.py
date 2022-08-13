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



h, w = map(int, inputSys().split())
A = [list(map(int, inputSys().split())) for _ in range(h)]
h2, w2 = map(int, inputSys().split())
B = [list(map(int, inputSys().split())) for _ in range(h2)]

if A == B:
    print("Yes")
    exit()

hh = h - h2
ww = w - w2

hc = list(itertools.combinations(range(h), h2))
wc = list(itertools.combinations(range(w), w2))

for i in hc:
    for j in wc:
        lst = []
        for k in range(h):
            if k not in i:
                continue
            tmp = []
            for l in range(w):
                if l not in j:
                    continue
                tmp.append(A[k][l])
            lst.append(tmp)
        if lst == B:
            print("Yes")
            exit()
print("No")
