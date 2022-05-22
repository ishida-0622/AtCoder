# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

dic = "abcdefghijklmnopqrstuvwxyz"
s = list(input())
t = list(input())

ln = len(s)
for i in range(ln):
    for j in range(26):
        if t[i] == dic[j]:
            t[i] = j
            break
for i in range(ln):
    for j in range(26):
        if s[i] == dic[j]:
            s[i] = j
            break

for i in range(26):
    if (s[0] + i) % 26 == t[0]:
        n = i

for i in range(ln):
    s[i] = (s[i] + n) % 26

if s == t:
    print("Yes")
else:
    print("No")