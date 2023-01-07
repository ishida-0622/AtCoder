import sys
sys.setrecursionlimit(7*10**5)

def dfs(now):
    for next_node in node[now]:
        if is_sean[next_node]:
            continue
        is_sean[next_node] = True
        dfs(next_node)

n, m = map(int, input().split())
node = [[] for _ in range(n)]
is_sean = [False] * n
ans = 0

for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    node[a].append(b)
    node[b].append(a)

for i in range(n):
    if is_sean[i]:
        continue
    dfs(i)
    ans += 1

print(ans)
