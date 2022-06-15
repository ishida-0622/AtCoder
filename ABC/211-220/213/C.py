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



h, w, n = map(int, inputSys().split())
A, B = [], []
for i in range(n):
    a, b = map(int, inputSys().split())
    A.append([a, i])
    B.append([b, i])
A.sort()
B.sort()
i = 0
while i < n:
    j = 1
    tmp = A[i][0]
    if i != 0:
        A[i][0] = A[i-1][0] + 1
    else:
        A[i][0] = 1
    while i+j < n and tmp == A[i+j][0]:
        A[i+j][0] = A[i][0]
        j += 1
    i += j
i = 0
while i < n:
    j = 1
    tmp = B[i][0]
    if i != 0:
        B[i][0] = B[i-1][0] + 1
    else:
        B[i][0] = 1
    while i+j < n and tmp == B[i+j][0]:
        B[i+j][0] = B[i][0]
        j += 1
    i += j
A.sort(key=lambda x: x[1])
B.sort(key=lambda x: x[1])
for i in range(n):
    print(A[i][0], B[i][0])
