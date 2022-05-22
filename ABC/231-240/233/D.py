# import itertools # 順列全探索(nCr)
# import bisect # 二分探索
# import math
# import string
# a_z = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
# import copy # copy.copy copy.deepcopy
import sys
input = sys.stdin.readline # rstrip()
# sys.setrecursionlimit(10**6) # 再帰

def mapInt():return map(int, input().split())
def mapStr():return map(str, input().split())
def listMapInt():return list(map(int, input().split()))
def listMapStr():return list(map(str, input().split()))

n,k = mapInt()
lst = listMapInt()
dp = [[0,0] for _ in range(n)]
m = 0
for i in range(n):
    m += lst[i]
    dp[i][0] = m
    dp[i][1] = dp[i-1][1]
    l = m*1
    if l == k:
        dp[i][1] += 1
    for j in range(i):
        l -= lst[j]
        if l == k:
            dp[i][1] += 1

print(dp[n-1][1])