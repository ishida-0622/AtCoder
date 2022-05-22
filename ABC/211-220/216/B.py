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

n = int(input())
lst = [input() for _ in range(n)]
if len(set(lst)) == n:
    print("No")
else:
    print("Yes")