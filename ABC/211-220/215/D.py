# # import itertools # 順列全探索(nCr) permutations()
# # import bisect # 二分探索
# # import math
# # import string
# # a_z = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
# # A_Z = string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
# # import copy # copy.deepcopy()
# import sys
# input = sys.stdin.readline # rstrip() <- 改行コード削除
# # sys.setrecursionlimit(10**6) # 再帰

# def intIn():return int(input())
# def strIn():return input().rstrip()
# def mapInt():return map(int, input().rstrip().split())
# def mapStr():return map(str, input().rstrip().split())
# def listMapInt():return list(map(int, input().rstrip().split()))
# def listMapStr():return list(map(str, input().rstrip().split()))
# def yesNo(flag, yes="Yes", no="No"):print(yes) if flag else print(no)



# n, m = mapInt()
# lst = listMapInt()
# ans = set()
# ans.add(2)
# for i in range(3,m):
#     flg = True
#     for j in ans:
#         if i % j == 0:
#             flg = False
#             break
#     if flg:
#         if i not in lst:
#             ans.add(i)

# reList = []
# for i in lst:
#     for j in ans:
#         if i % j == 0:
#             reList.append(j)
# for i in reList:
#     ans.remove(i)

# ans.add(1)

# print(len(ans))
# ans = sorted(list(ans))
# for i in ans:
#     print(i)
