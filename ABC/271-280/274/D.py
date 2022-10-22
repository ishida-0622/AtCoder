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
max___ = max # minとmaxの見分けがつきやすいようにラッパー
___min = min
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
def lcm(a,b): return a*b // gcd(a,b)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート



N, x, y = map(int, inputSys().split())
lst = list(map(int, inputSys().split()))
dpX = [[False] * 20000 for _ in range(-(-N//2)+1)]
dpY = [[False] * 20000 for _ in range(N//2+1)]
dpX[1][10000+lst[0]] = True
dpY[0][10000] = True
for i, val in enumerate(lst):
    if i == 0:
        continue
    if i % 2 == 0:
        for j in range(20000):
            if dpX[i//2][j]:
                if j+val < 20000:
                    dpX[i//2+1][j+val] = True
                if j-val >= 0:
                    dpX[i//2+1][j-val] = True
    else:
        for j in range(20000):
            if dpY[i//2][j]:
                if j+val < 20000:
                    dpY[i//2+1][j+val] = True
                if j-val >= 0:
                    dpY[i//2+1][j-val] = True

YesNo(dpX[-1][10000+x] and dpY[-1][10000+y])
