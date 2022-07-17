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


def r(level, m):
    if level == 0:
        return
    red[level-1] += m
    red[level] -= m
    blue[level] += x * m

def b(level, m):
    if level == 0:
        return
    red[level-1] += m
    blue[level-1] += y * m
    blue[level] -= m

n, x, y = map(int, inputSys().split())
n -= 1
red = [0] * 10
blue = [0] * 10
red[n] = 1
while sum(red[1:]) + sum(blue[1:]) > 0:
    for i in range(n, -1, -1):
        r(i, red[i])
    for i in range(n, -1, -1):
        b(i, blue[i])
print(blue[0])
