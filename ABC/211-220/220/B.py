# import itertools # 順列全探索(nCr) permutations()
# import bisect # 二分探索
# import math
# import string
# a_z = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
# import copy # copy.deepcopy()
import sys
input = sys.stdin.readline # rstrip() <- 改行コード削除
# sys.setrecursionlimit(10**6) # 再帰

def mapInt():return map(int, input().split())
def mapStr():return map(str, input().split())
def listMapInt():return list(map(int, input().split()))
def listMapStr():return list(map(str, input().split()))

k = int(input())
a,b = mapStr()
a,b = int(a,k), int(b,k)
print(a*b)