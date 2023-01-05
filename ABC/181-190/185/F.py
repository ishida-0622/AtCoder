from typing import TypeVar, Sequence, Callable

T = TypeVar("T")

class SegTree:
    def __init__(self, n: int, func: Callable[[int, int], T], e: T, init_val: Sequence[T]=None):
        """セグ木. 前提条件 -> func(func(x, y), z) = func(x, func(y, z))

        Args:
            n (int) : 要素数.
            func : 区間に対して行う処理.
            e : 単位元. min -> inf, max -> -inf, sum -> 0, mul -> 1, gcd -> 0, lcm -> 1, xor -> 0.
            init_val : 初期値. Noneの場合はeで初期化される.
        """
        self.n = n
        self.func = func
        self.e = e
        self.log = (n - 1).bit_length()
        self.size = 1 << self.log
        self.tree = [self.e] * (self.size << 1)
        if init_val is not None:
            for i in range(self.n):
                self.tree[self.size + i] = init_val[i]
            for i in range(self.size - 1, 0, -1):
                self.tree[i] = self.func(self.tree[i << 1], self.tree[i << 1 | 1])

    def set(self, p: int, x: T):
        """p番目の要素をxに変更. Ο(log N)

        Args:
            p (int): index
            x (int): value
        """
        p += self.size
        self.tree[p] = x
        while p:
            self.tree[p >> 1] = self.func(self.tree[p], self.tree[p ^ 1])
            p >>= 1

    def get(self, p: int):
        """p番目の要素を取得. Ο(1)

        Args:
            p (int): index

        Returns:
            T: p番目の要素
        """
        return self.tree[p + self.size]

    def prod(self, l: int, r: int):
        """区間[l, r)に対してfuncを適用したものを返す. Ο(log N)

        Args:
            l (int): index
            r (int): index

        Returns:
            any: 区間[l, r)に対してfuncを適用したもの. l=rの場合はe
        """
        sml, smr = self.e, self.e
        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                sml = self.func(sml, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.func(self.tree[r], smr)
            l >>= 1
            r >>= 1
        return self.func(sml, smr)

    def all_prod(self):
        """全要素に対してfuncを適用したものを返す. Ο(1)

        Returns:
            any: 全要素に対してfuncを適用したもの
        """
        return self.tree[1]


n, Q = map(int, input().split())
lst = list(map(int, input().split()))
seg_tree = SegTree(n, lambda a, b: a ^ b, 0, lst)

for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        seg_tree.set(x-1, seg_tree.get(x-1) ^ y)
    else:
        print(seg_tree.prod(x-1, y))
