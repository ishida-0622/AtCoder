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



n = int(inputSys())
s = inputSys().rstrip()
W = list(map(int, inputSys().split()))
kodomo = []
otona = []
for i, val in enumerate(s):
    if val == "0":
        kodomo.append(W[i])
    else:
        otona.append(W[i])
kodomo.sort()
otona.sort()
if len(otona) == 0 or len(kodomo) == 0 or kodomo[-1] < otona[0]:
    print(n)
    exit()
m = kodomo[-1] - otona[0]
k = inf
o = minf
for i in range(len(kodomo)-1, -1, -1):
    if kodomo[i] >= otona[0]:
        k = i
for i in range(len(otona)):
    if otona[i] <= kodomo[-1]:
        o = i
if k == inf:
    print(max(len(kodomo), len(otona)))
    exit()
otona = otona[0:o+1]
kodomo = kodomo[k:]
# print(kodomo, otona, sep="\n")
lst = [[val, "1"] for val in otona]
for val in kodomo:
    lst.append([val, "0"])
lst.sort()
ans = max(len(kodomo), len(otona))
o = 0
k = len(kodomo)
i = 0
while i < len(lst):
    cnt = 0
    while i+cnt < len(lst) and lst[i][0] == lst[i+cnt][0]:
        if lst[i+cnt][1] == "0":
            k -= 1
        else:
            o += 1
        cnt += 1
    ans = max(ans, len(lst)-o-k)
    i += cnt

ans += n - len(lst)
print(ans)
