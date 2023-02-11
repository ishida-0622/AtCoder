def dfs(now):
    if is_seen[now]:
        return
    if now in A:
        dfs(now+1)
    is_seen[now] = True
    ans.append(now)

n, m = map(int, input().split())
A = list(map(int, input().split()))
is_seen = [False] * (n+1)
ans = []

for i in range(1, n+1):
    dfs(i)

print(*ans)
