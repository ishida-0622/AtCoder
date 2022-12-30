from heapq import heappush, heappop

class WeightedGraph:
    def __init__(self, n: int):
        self.n = n
        self.node: list[list[tuple[int, int]]] = [[] * n for _ in range(n)]
        self.dist = [float("inf")] * n

    def union(self, x: int, y: int, cost: int, is_directed: bool = False):
        self.node[x].append((y, cost))
        if not is_directed:
            self.node[y].append((x, cost))

    def dijkstra(self, start: int):
        self.dist = [float("inf")] * self.n
        # self.dist[start] = 0
        que: list[tuple[int, int]] = []
        for next, c in self.node[start]:
            if c >= 0:
                heappush(que, (c, next))
        while que:
            cost, now = heappop(que)
            if cost > self.dist[now]:
                continue
            self.dist[now] = cost
            for next, c in self.node[now]:
                if c != float("inf"):
                    if c + cost >= self.dist[next]:
                        continue
                    heappush(que, (c + cost, next))
        return self.dist




n, m = map(int, input().split())
g = WeightedGraph(n)

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    g.union(a, b, c, True)

for i in range(n):
    d = g.dijkstra(i)
    print(d[i] if d[i] != float("inf") else -1)
