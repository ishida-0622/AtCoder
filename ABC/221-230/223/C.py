# import itertools # 順列全探索(nCr)
# import bisect # 二分探索
# import math
# import string
# a_z = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
# import copy
import sys
input = sys.stdin.readline # rstrip()
# sys.setrecursionlimit(10**6)

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
cntLst = []
for i in lst:
    cnt += i[0] / i[1]
    cntLst.append(i[0] / i[1])
cnt /= 2
idx = 0
ans = 0
while cnt > 0:
    if cnt >= cntLst[idx]:
        cnt -= cntLst[idx]
        ans += lst[idx][0]
        idx += 1
    else:
        ans += lst[idx][0] * cnt / cntLst[idx]
        break
print(ans)