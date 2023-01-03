inf = float("inf")

class WarshallFloyd:
    def __init__(self, n: int):
        self.n = n
        self.dist = [[inf] * n for _ in range(n)]
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
