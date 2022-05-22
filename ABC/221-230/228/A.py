import sys
input = sys.stdin.readline

s,t,x = map(int, input().split())
ans = ""

if s < t:
    if s <= x < t:
        ans = "Yes"
    else:
        ans = "No"
else:
    if t <= x < s:
        ans = "No"
    else:
        ans = "Yes"

print(ans)