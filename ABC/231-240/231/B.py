import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

dic = {}
n = int(input())
lst = [input() for _ in range(n)]
for i in range(n):
    dic.setdefault(lst[i], 0)
for i in range(n):
    dic[lst[i]] += 1
print(max(dic.items(), key=lambda x: x[1])[0], end="")