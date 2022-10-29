import sys
inputSys = sys.stdin.readline
sys.setrecursionlimit(10**7)
import bisect
import string
import math
from math import gcd
from copy import deepcopy
from collections import deque
from collections import defaultdict
from itertools import combinations
from itertools import permutations
from itertools import accumulate
from functools import lru_cache
from decimal import Decimal, ROUND_HALF_UP
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
# Decimal(str(n)).quantize(Decimal("0.1"), ROUND_HALF_UP) <- 四捨五入



h, w, x, y = map(int, inputSys().split())
x -= 1
y -= 1
lst = [input() for _ in range(h)]
ans = 1
i, j = x-1, y
while i >= 0 and lst[i][j] == ".":
    ans += 1
    i -= 1
i = x+1
while i < h and lst[i][j] == ".":
    ans += 1
    i += 1
i, j = x, y-1
while j >= 0 and lst[i][j] == ".":
    ans += 1
    j -= 1
j = y+1
while j < w and lst[i][j] == ".":
    ans += 1
    j += 1
print(ans)
