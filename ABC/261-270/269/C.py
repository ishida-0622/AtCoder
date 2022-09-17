import sys
inputSys = sys.stdin.readline
sys.setrecursionlimit(10**7)
from copy import deepcopy
from collections import deque
from itertools import combinations
from itertools import permutations
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



n = bin(int(input()))[2:]
lst = []
ans = []
for i, val in enumerate(n):
    if val == "1":
        lst.append(i)

for i in range(len(lst)+1):
    ls = list(combinations(lst, i))
    for val in ls:
        s = ""
        for k in range(len(n)):
            if k in val:
                s += "1"
            else:
                s += "0"
        ans.append(int(s, 2))
print(*sorted(ans), sep="\n")
