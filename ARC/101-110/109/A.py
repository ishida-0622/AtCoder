from heapq import heappush, heappop

class Dijkstra:
    def __init__(self, n: int):
        self.n = n
        self.cost = [[-1] * n for _ in range(n)]
        self.dist = [float("inf")] * n

    def union(self, x: int, y: int, cost: int, is_directed: bool = False):
        self.cost[x][y] = cost
        if not is_directed:
            self.cost[y][x] = cost

    def dijkstra(self, start: int):
        self.dist = [float("inf")] * self.n
        self.dist[start] = 0
        que: list[tuple[int, int]] = []
        for i, c in enumerate(self.cost[start]):
            if c >= 0:
                heappush(que, (c, i))
        while que:
            cost, now = heappop(que)
            if self.dist[now] < float("inf"):
                continue
            self.dist[now] = cost
            for next, c in enumerate(self.cost[now]):
                if c >= 0:
                    heappush(que, (c + self.dist[now], next))
        return self.dist



a, b, x, y = map(int, input().split())
a -= 1
b -= 1
g = Dijkstra(200)

for i in range(100):
    g.union(i, 100+i, x)
    if i < 99:
        g.union(i+1, i+100, x)
        g.union(i, i+1, y)
        g.union(i+100, i+101, y)

d = g.dijkstra(a)
print(d[100+b])
