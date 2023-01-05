from collections import defaultdict

class UnionFind:
    """Union-Find Tree"""

    def __init__(self, n: int):
        """初期化 Ο(N)

        Args:
            n (int): 頂点数
        """
        self.n = n
        self.parents = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    def union(self, x: int, y: int):
        """頂点xとyを繋ぐ Ο(log N)

        Args:
            x (int): 頂点
            y (int): 頂点

        Returns:
            bool: xとyがすでに同じ集合に属していた場合False, そうでない場合True
        """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parents[y] = x
        self.siz[x] += self.siz[y]
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        return True

    def find(self, x: int):
        """頂点xが属する集合の根を返す Ο(log N)

        Args:
            x (int): 頂点

        Returns:
            int: 頂点xが属する集合の根
        """
        if self.parents[x] == -1:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def same(self, x: int, y: int):
        """頂点xとyが同じ集合に属するかを返す Ο(log N)

        Args:
            x (int): 頂点
            y (int): 頂点

        Returns:
            bool: 頂点xとyが同じ集合に属する場合True, そうでない場合False
        """
        return self.find(x) == self.find(y)

    def size(self, x: int):
        """頂点xが所属する集合の要素数を返す Ο(log N)

        Args:
            x (int): 頂点

        Returns:
            int: 頂点xが所属する集合の要素数
        """
        return self.siz[self.find(x)]

    def members(self, x: int):
        """頂点xが属する集合を返す Ο(N log N)

        Args:
            x (int): 頂点

        Returns:
            list[int]: 頂点xが属する集合
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """根の一覧を返す Ο(N)

        Returns:
            list[int]: 根の一覧
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """集合の数を返す Ο(N)

        Returns:
            int: 集合の数
        """
        return len(self.roots())

    def all_group_members(self):
        """全ての集合と属する頂点を返す Ο(N log N)

        Returns:
            defaultdict[int, list[int]]: key: 根, value: その集合に属する頂点
        """
        group_members: defaultdict[int, list[int]] = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        """Ο(N log N)

        Returns:
            str: root: value
        """
        return "\n".join(f"{k}: {v}" for k, v in self.all_group_members().items())




n, m = map(int, input().split())
uf = UnionFind(n)
lst = list(map(int, input().split()))
ans = 0

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    uf.union(x, y)

for i, v in enumerate(lst):
    if uf.same(i, v-1):
        ans += 1

print(ans)
