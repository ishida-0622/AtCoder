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
sumNum = 0
if N % 2 == 0:
    sumNum = (1 + N) * (N // 2)
else:
    sumNum = (1 + N) * (N // 2) + (N // 2 + 1)

sumA = sumB = 0
a = b = 0
for i in range(N, -1, -1):
    if i % A == 0:
        a = i
        break
if N // A % 2 == 0:
    sumA = (A + a) * ((N // A) // 2)
else:
    sumA = ((A + a) * ((N // A) // 2)) + (A + a) // 2

for i in range(N, -1, -1):
    if i % B == 0:
        b = i
        break
if N // B % 2 == 0:
    sumB = (B + b) * ((N // B) // 2)
else:
    sumB = (B + b) * ((N // B) // 2) + (B + b) // 2

AB = A * B // math.gcd(A,B)
ab = 0
sumAB = 0
if AB <= N:
    for i in range(N, -1, -1):
        if i % AB == 0:
            ab = i
            break
    if N // AB % 2 == 0:
        sumAB = (AB + ab) * ((N // AB) // 2)
    else:
        sumAB = (AB + ab) * ((N // AB) // 2) + (AB + ab) // 2


print(sumNum - (sumA + sumB - sumAB))
