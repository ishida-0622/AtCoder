lst = list(map(int, input().split()))
ans = 0
for i in range(64):
    ans += lst[i] * 2**i
print(ans)
