# import itertools # 順列全探索(nCr)
# import bisect # 二分探索
# import math
# import string
# a_z = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
import copy # copy.copy copy.deepcopy
import sys
# input = sys.stdin.readline # rstrip()
# sys.setrecursionlimit(10**6) # 再帰

def mapInt():return map(int, input().split())
def mapStr():return map(str, input().split())
def listMapInt():return list(map(int, input().split()))
def listMapStr():return list(map(str, input().split()))

l,r = mapInt()
l -= 1
r -= 1
s = input()
ln = len(s)
ln -= r+1

for i in range(l):
    print(s[i],end="")
for i in range(r,l-1,-1):
    print(s[i],end="")
for i in range(ln):
    print(s[r+i+1],end="")
print()