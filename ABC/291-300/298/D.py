import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(7*10**5)
import string
import math
from math import gcd, sqrt, floor, ceil, sin, cos, tan, pi
from copy import deepcopy
from collections import deque, defaultdict, Counter
from itertools import combinations, permutations, accumulate
from bisect import bisect_left, bisect_right, insort_left, insort_right
from heapq import heapify, heappop, heappush
from functools import lru_cache, reduce
from decimal import Decimal, ROUND_HALF_UP
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
az = string.ascii_lowercase
AZ = string.ascii_uppercase
aZ = string.ascii_letters
zero_nine = string.digits
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
def yes(yes="Yes"): print(yes);exit()
def no(no="No"): print(no);exit()
def lcm(a,b): return a*b // gcd(a,b)
# Decimal(str(n)).quantize(Decimal("0.1"), ROUND_HALF_UP) <- 四捨五入



class ModInt:
    def __init__(self, x):
        self.x = x % mod

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        return (
            ModInt(self.x + other.x) if isinstance(other, ModInt) else
            ModInt(self.x + other)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x) if isinstance(other, ModInt) else
            ModInt(self.x - other)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x) if isinstance(other, ModInt) else
            ModInt(self.x * other)
        )

    def __truediv__(self, other):
        return (
            ModInt(
                self.x * pow(other.x, mod - 2, mod)
            ) if isinstance(other, ModInt) else
            ModInt(self.x * pow(other, mod - 2, mod))
        )

    def __pow__(self, other):
        return (
            ModInt(pow(self.x, other.x, mod)) if isinstance(other, ModInt) else
            ModInt(pow(self.x, other, mod))
        )

    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x) if isinstance(other, ModInt) else
            ModInt(other - self.x)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(
                other.x * pow(self.x, mod - 2, mod)
            ) if isinstance(other, ModInt) else
            ModInt(other * pow(self.x, mod - 2, mod))
        )

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, mod)) if isinstance(other, ModInt) else
            ModInt(pow(other, self.x, mod))
        )



ans = ModInt(1)
que = deque([1])

for _ in range(int(input())):
    query = list(map(int, input().split()))
    q = query[0]
    if q == 1:
        x = query[1]
        ans *= 10
        ans += x
        que.append(x)
    elif q == 2:
        tmp = que.popleft()
        ans -= pow(10, len(que), mod) * tmp
    else:
        print(ans)
