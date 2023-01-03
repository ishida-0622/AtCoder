inf = float("inf")

class WarshallFloyd:
    def __init__(self, n: int):
        self.n = n
        self.dist = [[inf] * n for _ in range(n)]
        self.prev = [[-1] * n for _ in range(n)]
        for i in range(n):
            self.dist[i][i] = 0

    def union(self, x: int, y: int, cost: int = 1, is_directed: bool = False):
        self.dist[x][y] = cost
        self.prev[x][y] = x
        if not is_directed:
            self.dist[y][x] = cost
            self.prev[y][x] = y

    def warshall_floyd(self):
        """ワーシャルフロイド法による探索 Ο(N^3)"""
        is_negative = False
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.dist[i][k] + self.dist[k][j] < self.dist[i][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]
                        self.prev[i][j] = self.prev[k][j]
        # 負閉路検出
        for i in range(self.n):
            if self.dist[i][i] < 0:
                is_negative = True
        return self.dist, is_negative

    def get_path(self, start: int, goal: int):
        """
        最短経路の復元\n
        warshall_floydが実行されているのが前提
        """
        path = []
        now = goal
        while now != start:
            path.append(now)
            now = self.prev[start][now]
        path.append(start)
        path.reverse()
        return path
