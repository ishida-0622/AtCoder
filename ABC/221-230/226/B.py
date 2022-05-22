# import itertools # 順列全探索(nCr)
# import bisect # 二分探索
# import math
# import string
# a_z = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
# import copy
import sys
input = sys.stdin.readline # .rstrip()
# sys.setrecursionlimit(10**6)

n = int(input())
lst = [input().rstrip() for _ in range(n)]
print(len(set(lst)))