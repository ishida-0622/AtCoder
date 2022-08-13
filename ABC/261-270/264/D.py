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



s = list(inputSys().rstrip())
S = "atcoder"

dic = {}
for i, val in enumerate(s):
    dic[val] = i

cnt = 0
while s[0] != "a":
    i = dic["a"]
    dic[s[i-1]] = i
    dic["a"] = i-1
    s[i] = s[i-1]
    s[i-1] = "a"
    cnt += 1

while s[1] != "t":
    i = dic["t"]
    dic[s[i-1]] = i
    dic["t"] = i-1
    s[i] = s[i-1]
    s[i-1] = "t"
    cnt += 1

while s[2] != "c":
    i = dic["c"]
    dic[s[i-1]] = i
    dic["c"] = i-1
    s[i] = s[i-1]
    s[i-1] = "c"
    cnt += 1

while s[3] != "o":
    i = dic["o"]
    dic[s[i-1]] = i
    dic["o"] = i-1
    s[i] = s[i-1]
    s[i-1] = "o"
    cnt += 1

while s[4] != "d":
    i = dic["d"]
    dic[s[i-1]] = i
    dic["d"] = i-1
    s[i] = s[i-1]
    s[i-1] = "d"
    cnt += 1

while s[5] != "e":
    i = dic["e"]
    dic[s[i-1]] = i
    dic["e"] = i-1
    s[i] = s[i-1]
    s[i-1] = "e"
    cnt += 1
print(cnt)
