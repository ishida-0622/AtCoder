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



a_z = string.ascii_lowercase

def f(dep, bit):
    if dep == n:
        res = 0
        ls = []
        for i in range(n):
            if bit[i] == "1":
                ls.append(lst[i])
        for s in a_z:
            cnt = 0
            for val in ls:
                if s in val:
                    cnt += 1
            if cnt == k:
                res += 1
        return res
    return max(f(dep+1, bit+"0"), f(dep+1, bit+"1"))

n, k = map(int, inputSys().split())
lst = [inputSys().rstrip() for _ in range(n)]
ans = max(f(1, "0"), f(1, "1"))
print(ans)
