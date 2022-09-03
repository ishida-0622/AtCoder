import sys
inputSys = sys.stdin.readline
sys.setrecursionlimit(10**7)
from copy import deepcopy
from collections import deque
import itertools  # combinations() <- nCr, permutations() <- nPr
import bisect
import math
from functools import lru_cache
import string
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート



s = list(inputSys().rstrip())
if s[0] == "1":
    print("No")
    exit()

if s[3] == "0":
    if s[6] == "1" and ((s[1] == "1" or s[7] == "1") or (s[4] == "1") or (s[2] == "1" or s[8] == "1") or (s[5] == "1") or (s[9] == "1")):
        print("Yes")
        exit()

if s[1] == "0" and s[7] == "0":
    if (s[3] == "1" or s[6] == "1") and ((s[4] == "1") or (s[2] == "1" or s[8] == "1") or (s[5] == "1") or (s[9] == "1")):
        print("Yes")
        exit()

if s[4] == "0":
    if (s[3] == "1" or s[6] == "1" or (s[1] == "1" or s[7] == "1")) and ((s[2] == "1" or s[8] == "1") or (s[5] == "1") or (s[9] == "1")):
        print("Yes")
        exit()

if s[2] == "0" and s[8] == "0":
    if (s[4] == "1") or (s[9] == "1") and (s[3] == "1" or s[6] == "1" or (s[1] == "1" or s[7] == "1") or s[4] == "1"):
        print("Yes")
        exit()

if s[5] == "0":
    if s[9] == "1" and (s[3] == "1" or s[6] == "1" or (s[1] == "1" or s[7] == "1") or s[4] == "1" or (s[2] == "1" or s[8] == "1")):
        print("Yes")
        exit()

print("No")
