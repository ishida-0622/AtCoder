import sys
inputSys = sys.stdin.readline
sys.setrecursionlimit(10**7)
import bisect
import string
import math
from math import gcd, sqrt
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



ans = 0
lst = [input() for _ in range(9)]
p = [i for i in range(81) if lst[i//9][i%9] == "#"]

com = list(combinations(p, 4))

for val in com:
    c = combinations(val, 2)
    d = sorted([pow(a//9 - b//9, 2) + pow(a%9 - b%9, 2) for a, b in c])
    if d[0] == d[3] and d[4] == d[5] and d[4] == d[0] * 2:
        ans += 1

print(ans)
