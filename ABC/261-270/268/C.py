import random
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



n = int(inputSys())
lst = list(map(int, inputSys().split()))
ans = 0

ls = sorted([(v-i)%n for i, v in enumerate(lst)])

dic = {}
for i in range(n):
    dic[i] = 0

for i in range(n):
    dic[ls[i]] += 1

for i in range(n):
    ans = max(ans, dic[i] + dic[(i+1)%n] + dic[(i-1)%n])

print(ans)
