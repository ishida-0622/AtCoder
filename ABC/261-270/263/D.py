import sys
inputSys = sys.stdin.readline
# sys.setrecursionlimit(10**7)
# from copy import deepcopy
# from collections import deque
# import itertools  # combinations() <- nCr, permutations() <- nPr
# import bisect
# import math
# from functools import lru_cache
# import string
# mod = 998244353
# mod2 = 1000000007
# inf = float("inf")
minf = -float("inf")
# def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート



n, L, R = map(int, inputSys().split())
lst = list(map(int, inputSys().split()))

# i番目まで全て置き換えた場合の差 +であるほど良い
Ln = [0]
# n-i番目まで全て置き換えた場合の差 +であるほど良い
Rn = [0]
for i in range(n):
    Ln.append(Ln[i] + (lst[i] - L))
    Rn.append(Rn[i] + (lst[-i-1] - R))

# i番目までを最適に選んだ場合の差と最適解のindex
maxLn = [[Ln[0], 0]]
# n-i番目までを最適に選んだ場合の差と最適解のindex
maxRn = [[Rn[0], 0]]

maxIdx = 0
for i in range(1,n+1):
    # i番目まで置き換えた方が最適ならindexを更新
    if Ln[i] > Ln[maxIdx]:
        maxIdx = i
    maxLn.append([max(Ln[i], maxLn[i-1][0]), maxIdx])
maxIdx = 0
for i in range(1,n+1):
    # n-i番目まで置き換えた方が最適ならindexを更新
    if Rn[i] > Rn[maxIdx]:
        maxIdx = i
    maxRn.append([max(Rn[i], maxRn[i-1][0]), maxIdx])

# Lmax = minf
Lidx = 0
# Rmax = minf
Ridx = 0
sumMax = minf

# 左からi(0 <= i <= n)番目までを置き換えた場合の最適解
for i in range(n+1):
    # 最適だったら差とindexを更新
    if sumMax <= maxLn[i][0] + maxRn[-i-1][0]:
        sumMax = maxLn[i][0] + maxRn[-i-1][0]
        Lidx = maxLn[i][1]
        Ridx = maxRn[-i-1][1]

# TLEだけど制約が小さければACできるコード Ο(N^2)
# for i in range(n+1):
#     # ここの処理重すぎるからTLE
#     Lmax = max(Ln[0:i+1])
#     Rmax = max(Rn[0:n-i+1])

#     if Rmax + Lmax >= sumMax:
#         sumMax = Rmax + Lmax
#         if Lmax == Ln[i]:
#             Lidx = i
#         if Rmax == Rn[n-i]:
#             Ridx = n-i

lst = ([L] * (Lidx)) + lst[Lidx:(n-Ridx)] + ([R] * (Ridx))

print(sum(lst))
