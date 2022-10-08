import sys
inputSys = sys.stdin.readline
sys.setrecursionlimit(10**7)
from copy import deepcopy
from collections import deque
from itertools import combinations
from itertools import permutations
import bisect
import math
from math import gcd
from functools import lru_cache
import string
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
def lcm(a,b): return a*b // gcd(a,b)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート



n = int(inputSys())
lst = sorted(list(map(int, inputSys().split())))
even = [val for val in lst if val % 2 == 0]
odd = [val for val in lst if val % 2 == 1]

if n == 2 and sum(lst) % 2 == 1:
    print(-1)
    exit()

even_sum = even[-1] + even[-2] if len(even) > 1 else 0
odd_sum = odd[-1] + odd[-2] if len(odd) > 1 else 0

print(max(even_sum, odd_sum))
