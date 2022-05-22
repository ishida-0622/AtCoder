# import itertools # 順列全探索(nCr)
# import bisect # 二分探索
# import math
# import string
# a_z = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
# import copy
# import sys
# input = sys.stdin.readline # rstrip()
# sys.setrecursionlimit(10**6)

s = input()
t = input()
ln = len(s)
ans = "No"
lst = []
if s != t:
    for i in range(ln):
        if s[i] != t[i]:
            lst.append([i,s[i],t[i]])
    if len(lst) == 2 and lst[0][0]+1 == lst[1][0] and lst[0][1] == lst[1][2] and lst[0][2] == lst[1][1]:
        ans = "Yes"
else:
    ans = "Yes"
print(ans)