import sys
inputSys = sys.stdin.readline
# sys.setrecursionlimit(10**7)
from copy import deepcopy
import itertools  # combinations() <- nCr, permutations() <- nPr
import bisect  # 二分探索
import math  # factorial() <- 階乗, sqrt() <- 平方根
from functools import lru_cache # <- メモ化再帰 @lru_cache
import string
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート



N, A, B = map(int, inputSys().split())

sumNum = N * (N + 1) // 2
sumA = A * (N // A * (N // A + 1) // 2)
sumB = B * (N // B * (N // B + 1) // 2)
AB = A * B // math.gcd(A,B)
sumAB = AB * (N // AB * (N // AB + 1) // 2)
print(sumNum - (sumA + sumB - sumAB))
