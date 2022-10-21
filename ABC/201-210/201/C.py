import sys
inputSys = sys.stdin.readline
sys.setrecursionlimit(10**7)
from copy import deepcopy
from collections import deque
from collections import defaultdict
from itertools import combinations
from itertools import permutations
from itertools import accumulate
import bisect
import math
from math import gcd
from functools import lru_cache
import string
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
max___ = max
___min = min
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
def lcm(a,b): return a*b // gcd(a,b)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート



s = inputSys().rstrip()
flags = [1 if val == "o" else 0 if val == "?" else -1 for val in s]
ans = 0

for i in range(10000):
    tmp = map(int, str(i).zfill(4))
    lst = [False] * 10
    f = True
    for v in tmp:
        lst[v] = True
    for i, v in enumerate(lst):
        if v and flags[i] == -1:
            f = False
        if not v and flags[i] == 1:
            f = False
    if f:
        ans += 1

print(ans)
