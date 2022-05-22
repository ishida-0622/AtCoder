import itertools
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

n,m = map(int, input().split())

lst1 = [list(sorted(map(int, input().split()))) for _ in range(m)]
lst2 = [list(map(int, input().split())) for _ in range(m)]
lst3 = list(itertools.permutations(range(1,n+1)))
lst1.sort()
# print(lst1,lst2,lst3)
flg = False
if m > 1:
    ln = len(lst3)
    for i in range(ln):
        lst = []
        for j in range(m):
            hoge = sorted([lst3[i][lst2[j][0]-1], lst3[i][lst2[j][1]-1]])
            lst.append(hoge)
        lst.sort()
        # print(lst1,lst)
        if lst == lst1:
            flg = True
            break
else:
    flg = True

if flg:
    print("Yes")
else:
    print("No")