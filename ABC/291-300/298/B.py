import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(7*10**5)
import string
import math
from math import gcd, sqrt, floor, ceil, sin, cos, tan, pi
from copy import deepcopy
from collections import deque, defaultdict, Counter
from itertools import combinations, permutations, accumulate, groupby
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
def lcm(a: int, b: int): return a*b // gcd(a,b)
def round(n: int, d: int = 0): return float(Decimal(n).quantize(Decimal(f"1e{d}"), ROUND_HALF_UP))



def main():
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]
    B = [list(map(int, input().split())) for _ in range(n)]
    A_1 = []
    A_2 = []
    A_3 = []
    for i in range(n):
        a_1 = []
        a_2 = []
        a_3 = []
        for j in range(n):
            a_1.append(A[n-1-j][i])
            a_2.append(A[n-1-i][n-1-j])
            a_3.append(A[j][n-1-i])
        A_1.append(a_1)
        A_2.append(a_2)
        A_3.append(a_3)

    ans = True
    for i in range(n):
        for j in range(n):
            if A[i][j] == 1 and B[i][j] == 0:
                ans = False
    if ans:
        yes()

    ans = True
    for i in range(n):
        for j in range(n):
            if A_1[i][j] == 1 and B[i][j] == 0:
                ans = False
    if ans:
        yes()

    ans = True
    for i in range(n):
        for j in range(n):
            if A_2[i][j] == 1 and B[i][j] == 0:
                ans = False
    if ans:
        yes()

    ans = True
    for i in range(n):
        for j in range(n):
            if A_3[i][j] == 1 and B[i][j] == 0:
                ans = False
    if ans:
        yes()

    no()




if __name__ == "__main__":
    main()
