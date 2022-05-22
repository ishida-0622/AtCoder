import sys
input = sys.stdin.readline

a, b = map(str, input().split())

minLen = min(len(a),len(b))
flag = False

for i in range(1, minLen+1):
    if int(a[len(a)-i]) + int(b[len(b)-i]) >= 10:
        flag = True
        break

if flag:
    print("Hard")
else:
    print("Easy")
