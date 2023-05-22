from collections import deque

class Graph:
    def __init__(self, n: int):
        self.n = n
        self.node: list[list[int]] = [[] for _ in range(n)]
        self.is_seen = [False] * n
        self.prev = [-1] * n

    def union(self, x: int, y: int, is_directed: bool = False):
        self.node[x].append(y)
        if not is_directed:
            self.node[y].append(x)

    def bfs(self, start: int, goal: int):
        self.is_seen = [False] * self.n
        self.is_seen[start] = True
        que: deque[tuple[int, int]] = deque([(start, 0)])
        while que:
            now, dist = que.popleft()
            if now == goal:
                return dist
            for next in self.node[now]:
                if self.is_seen[next]:
                    continue
                self.is_seen[next] = True
                que.append((next, dist+1))
        return -1

    def bfs_with_root(self, start: int, goal: int):
        self.is_seen = [False] * self.n
        self.prev = [-1] * self.n
        self.is_seen[start] = True
        que: deque[tuple[int, int]] = deque([(start, 0)])
        while que:
            now, dist = que.popleft()
            if now == goal:
                # 経路復元
                root = []
                while now != -1:
                    root.append(now)
                    now = self.prev[now]
                root.reverse()
                return dist, root
            for next in self.node[now]:
                if self.is_seen[next]:
                    continue
                self.is_seen[next] = True
                self.prev[next] = now
                que.append((next, dist+1))
        return -1, []
