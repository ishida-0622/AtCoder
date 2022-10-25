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



n = int(inputSys())
lst = list(map(int, inputSys().split()))
ans = 0
mod200 = [val % 200 for val in lst]

dic = {i: 0 for i in range(0, 200)}

for v in mod200:
    dic[v] += 1

ans = 0
for v in dic.values():
    ans += max___(v * (v-1) // 2, 0)

print(ans)
