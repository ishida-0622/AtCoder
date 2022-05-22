# import itertools # 順列全探索(nCr) permutations()
# import bisect # 二分探索
# import math
# import string
# a_z = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
# A_Z = string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
# import copy # copy.deepcopy()
from os import lstat
import sys
input = sys.stdin.readline # rstrip() <- 改行コード削除
# sys.setrecursionlimit(10**6) # 再帰

def intIn():return int(input())
def strIn():return input().rstrip()
def mapInt():return map(int, input().rstrip().split())
def mapStr():return map(str, input().rstrip().split())
def listMapInt():return list(map(int, input().rstrip().split()))
def listMapStr():return list(map(str, input().rstrip().split()))
def yesNo(flag, yes="Yes", no="No"):print(yes) if flag else print(no)



s,t = mapInt()
ans = 0
lst = []
for i in range(s+1):
    for j in range(s+1):
        for k in range(s+1):
            if i+j+k <= s:
                lst.append((i,j,k))
            else:
                break

for i in lst:
    a,b,c = i
    if a*b*c <= t:
        ans += 1
print(ans)