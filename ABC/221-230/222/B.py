n,p = map(int, input().split())
point = list(map(int, input().split()))
ans = 0
for i in point:
    if i < p:
        ans += 1
print(ans)