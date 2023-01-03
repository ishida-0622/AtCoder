class WarshallFloyd:
    def __init__(self, n: int):
        self.n = n
        self.dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            self.dist[i][i] = 0

    def union(self, x: int, y: int, cost: int = 1, is_directed: bool = False):
        self.dist[x][y] = cost
        if not is_directed:
            self.dist[y][x] = cost

    def warshall_floyd(self):
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    self.dist[i][j] = min(self.dist[i][j], self.dist[i][k] + self.dist[k][j])
        return self.dist




h, w = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(10)]
wg = WarshallFloyd(10)
ans = 0
for i in range(10):
    for j in range(10):
        wg.union(i, j, cost[i][j], True)
d = wg.warshall_floyd()
for _ in range(h):
    lst = list(map(int, input().split()))
    for val in lst:
        if val != -1:
            ans += d[val][1]
print(ans)
