# import itertools # 順列全探索(nCr)
# import bisect # 二分探索
# import math
# import string
# a_z = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
# import copy
import sys
input = sys.stdin.readline # .rstrip()
# sys.setrecursionlimit(10**6)

n,w = map(int, input().split())
lst = sorted([list(map(int, input().split())) for _ in range(n)])
# lst.sort()
ans = 0
idx = n-1
m = 0
a = lst[idx][0]
b = lst[idx][1]
while m < w:
    ans += a * min(b,w-m)
    m += b
    if m < w:
        idx -= 1
        if idx < 0:
            break
        a = lst[idx][0]
        b = lst[idx][1]
print(ans)