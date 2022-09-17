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



n = int(inputSys())
lst = set(tuple(map(int, inputSys().split())) for _ in range(n))
ans = 0

def f(x,y):
    arri = [-1,-1,0,0,1,1]
    arrj = [-1,0,1,-1,0,1]
    for i in range(6):
        xx, yy = x + arri[i], y + arrj[i]
        if (xx, yy) in lst:
            lst.remove((xx, yy))
            f(xx,yy)

while len(lst) > 0:
    x, y = lst.pop()
    f(x,y)
    ans += 1

print(ans)
