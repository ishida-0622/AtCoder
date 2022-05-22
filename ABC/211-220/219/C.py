# import itertools # 順列全探索(nCr) permutations()
# import bisect # 二分探索
# import math
import string
a_z = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
# import copy # copy.deepcopy()
import sys
input = sys.stdin.readline # rstrip() <- 改行コード削除
# sys.setrecursionlimit(10**6) # 再帰

def mapInt():return map(int, input().split())
def mapStr():return map(str, input().split())
def listMapInt():return list(map(int, input().split()))
def listMapStr():return list(map(str, input().split()))

s = list(input().rstrip())
a_z = list(a_z)
dic = {s[i]: i for i in range(26)}
n = int(input())
lst = [list(input().rstrip()) for _ in range(n)]
for i in range(n):
    for j in range(len(lst[i])):
        lst[i][j] = dic[lst[i][j]]
lst.sort()
for i in lst:
    for j in i:
        print(s[j],end="")
    print()