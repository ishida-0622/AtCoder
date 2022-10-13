import random
import sys
import time
inputSys = sys.stdin.readline
sys.setrecursionlimit(10**7)
from copy import deepcopy
# from collections import deque
# from itertools import combinations
# from itertools import permutations
# import bisect
# import math
# from functools import lru_cache
# import string
# mod = 998244353
# mod2 = 1000000007
# inf = float("inf")
# minf = -float("inf")
# def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート



N, M = map(int, inputSys().split())
dic = {}
lst = []
for _ in range(M):
    x, y = map(int, inputSys().split())
    if x in dic:
        dic[x].append(y)
    else:
        dic[x] = [y]
    lst.append([x, y])

max_score = 0

def f(x, y, d):
    """点x, yから縦横斜めに存在する点を返す"""
    i = 1
    res = []
    flg = [True] * 8
    while True:
        if sum(flg) == 0 or (x+i > N and y+i > N and x-i < 0 and y-i < 0):
            return res
        if x+i in d and y in d[x+i]:
            if flg[0]:
                flg[0] = False
                res.append([x+i, y])
        if x-i in d and y in d[x-i]:
            if flg[1]:
                flg[1] = False
                res.append([x-i, y])
        if x in d and y+i in d[x]:
            if flg[2]:
                flg[2] = False
                res.append([x, y+i])
        if x in d and y-i in d[x]:
            if flg[3]:
                flg[3] = False
                res.append([x, y-i])
        if x+i in d and y+i in d[x+i]:
            if flg[4]:
                flg[4] = False
                res.append([x+i, y+i])
        if x-i in d and y+i in d[x-i]:
            if flg[5]:
                flg[5] = False
                res.append([x-i, y+i])
        if x+i in d and y-i in d[x+i]:
            if flg[6]:
                flg[6] = False
                res.append([x+i, y-i])
        if x-i in d and y-i in d[x-i]:
            if flg[7]:
                flg[7] = False
                res.append([x-i, y-i])
        i += 1

def ff(x1, y1, x2, y2, d):
    """点(x1, y1), (x2, y2)から"""
    res = []
    flg = [True] * 2
    xi1, yi1, xi2, yi2 = 0, 0, 0, 0
    if x1 > x2 and y1 > y2:
        # 左下
        xi1 = 1
        yi1 = -1
        xi2 = -1
        yi2 = 1
    if x1 > x2 and y1 < y2:
        # 左上
        xi1 = 1
        yi1 = 1
        xi2 = -1
        yi2 = -1
    if x1 < x2 and y1 < y2:
        # 右上
        xi1 = 1
        yi1 = -1
        xi2 = -1
        yi2 = 1
    if x1 < x2 and y1 > y2:
        # 右下
        xi1 = 1
        yi1 = 1
        xi2 = -1
        yi2 = -1
    if x1 > x2 and y1 == y2:
        # 左
        xi1 = 0
        yi1 = 1
        xi2 = 0
        yi2 = -1
    if x1 < x2 and y1 == y2:
        # 右
        xi1 = 0
        yi1 = 1
        xi2 = 0
        yi2 = -1
    if x1 == x2 and y1 < y2:
        # 上
        xi1 = 1
        yi1 = 0
        xi2 = -1
        yi2 = 0
    if x1 == x2 and y1 > y2:
        # 下
        xi1 = 1
        yi1 = 0
        xi2 = -1
        yi2 = 0
    i = 1
    while True:
        if not flg[0] and not flg[1] or i > N:
            break
        if flg[0] and x2 + xi1*i in d and y2 + yi1*i in d[x2 + xi1*i]:
            flg[0] = False
            res.append([x2 + xi1*i, y2 + yi1*i])
        if flg[1] and x2 + xi2*i in d and y2 + yi2*i in d[x2 + xi2*i]:
            flg[1] = False
            res.append([x2 + xi2*i, y2 + yi2*i])
        i += 1
    return res

def check(x1,y1,x2,y2,x3,y3,x4,y4,di):
    a = x1 - x4
    b = y1 - y4
    c = x3 - x4
    d = y3 - y4
    if a != 0 and b != 0:
        aa = range(1,a+1) if a >= 0 else range(-1, a-1, -1)
        bb = range(1,b+1) if b >= 0 else range(-1, b-1, -1)
        for val in zip(aa,bb):
            i, j = val
            if x1-i in di and y1-j in di[x1-i]:
                return False
        cc = range(1,c+1) if c >= 0 else range(-1, c-1, -1)
        dd = range(1,d+1) if d >= 0 else range(-1, d-1, -1)
        for val in zip(cc, dd):
            i, j = val
            if x3-i in di and y3-j in di[x3-i]:
                return False
    else:
        if a == 0:
            bb = range(1,b+1) if b >= 0 else range(-1, b-1, -1)
            for i in bb:
                if x1 in di and y1-i in di[x1]:
                    return False
            cc = range(1,c+1) if c >= 0 else range(-1,c-1,-1)
            for i in cc:
                if x3-i in di and y3 in di[x3-i]:
                    return False
        else:
            aa = range(1,a+1) if a >= 0 else range(-1, a-1, -1)
            for i in aa:
                if x1-i in di and y1 in di[x1-i]:
                    return False
            dd = range(1,d+1) if d >= 0 else range(-1,d-1,-1)
            for i in dd:
                if x3 in di and y3-i in di[x3]:
                    return False
    return True

def main():
    ans = []
    START_TIME = time.time()
    TIME_LIMIT = 4.5
    while True:
    # for _ in range(1):
        ls = deepcopy(lst)
        random.shuffle(ls)
        if time.time() - START_TIME > TIME_LIMIT:
            break
        tmp = []
        node = set()
        dic2 = deepcopy(dic)
        m = M*1
        # for i in range(m):
        i = -1
        while i < m-1:
            i += 1
            x, y = ls[i]
            res = f(x,y,dic2)
            random.shuffle(res)
            for val in res:
                xx, yy = val
                res2 = ff(x,y,xx,yy,dic2)
                random.shuffle(res2)
                for v in res2:
                    xxx, yyy = v
                    xxxx, yyyy = xxx + (x-xx), yyy + (y - yy)
                    # if xxxx == 28 and yyyy == 12:
                    #     if len(tmp) == 19:
                    #         pass
                    flg = True
                    a = x - xx
                    b = y - yy
                    if a != 0 and b != 0:
                        if (x,y,2) in node or (x,y,3) in node or (y,x,2) in node or (y,x,3) in node or (xx,yy,2) in node or (xx,yy,3) in node or (yy,xx,2) in node or (yy,xx,3) in node or (xxx,yyy,2) in node or (xxx,yyy,3) in node or (yyy,xxx,2) in node or (yyy,xxx,3) in node or (xxxx,yyyy,2) in node or (xxxx,yyyy,3) in node or (yyyy,xxxx,2) in node or (yyyy,xxxx,3) in node:
                            # print("false")
                            flg = False
                        if a > 0 and b > 0 or a < 0 and b < 0:
                            aa = range(1, a+1) if a >= 0 else range(-1,a-1,-1)
                            bb = range(1, b+1) if b >= 0 else range(-1,b-1,-1)
                            for val in zip(aa,bb):
                                j, k = val
                                if (x-j,y-k,2) in node or (xxx-j,yyy-k,2) in node:
                                    flg = False
                                    break
                        else:
                            aa = range(1, a+1) if a >= 0 else range(-1,a-1,-1)
                            bb = range(1, b+1) if b >= 0 else range(-1,b-1,-1)
                            for val in zip(aa,bb):
                                j, k = val
                                if (x-j,y-k,3) in node or (xxx-j,yyy-k,3) in node:
                                    flg = False
                                    break
                    else:
                        if (x,y,0) in node or (x,y,1) in node or (y,x,0) in node or (y,x,1) in node or (xx,yy,0) in node or (xx,yy,1) in node or (yy,xx,0) in node or (yy,xx,1) in node or (xxx,yyy,0) in node or (xxx,yyy,1) in node or (yyy,xxx,0) in node or (yyy,xxx,1) in node or (xxxx,yyyy,0) in node or (xxxx,yyyy,1) in node or (yyyy,xxxx,0) in node or (yyyy,xxxx,1) in node:
                            flg = False
                        if a == 0:
                            for j in range(1,b+1) if b >= 0 else range(-1,b-1,-1):
                                if (x, y-j, 0) in node or (xxx, yyy-j, 0) in node:
                                    flg = False
                                    break
                        else:
                            for j in range(1,a+1) if a >= 0 else range(-1,a-1,-1):
                                if (x-j, y, 1) in node or (xxx-j, yyy, 1) in node:
                                    flg = False
                                    break

                    a = xx - xxx
                    b = yy - yyy
                    if a != 0 and b != 0:
                        if (a > 0 and b > 0) or (a < 0 and b < 0):
                            aa = range(1, a+1) if a >= 0 else range(-1,a-1,-1)
                            bb = range(1, b+1) if b >= 0 else range(-1,b-1,-1)
                            for val in zip(aa,bb):
                                j, k = val
                                if (xx-j,yy-k,2) in node or (xxxx-j,yyyy-k,2) in node:
                                    flg = False
                                    break
                        else:
                            aa = range(1, a+1) if a >= 0 else range(-1,a-1,-1)
                            bb = range(1, b+1) if b >= 0 else range(-1,b-1,-1)
                            for val in zip(aa,bb):
                                j, k = val
                                if (xx-j,yy-k,3) in node or (xxxx-j,yyyy-k,3) in node:
                                    flg = False
                                    break
                    elif a == 0:
                        for j in range(1,b+1) if b >= 0 else range(-1,b-1,-1):
                            if (xx, yy-j, 0) in node or (xxxx, yyyy-j, 0) in node:
                                flg = False
                                break
                    else:
                        for j in range(1,a+1) if a >= 0 else range(-1,a-1,-1):
                            if (xx-j, yy, 1) in node or (xxxx-j, yyyy, 1) in node:
                                flg = False
                                break

                    if flg and check(x,y,xx,yy,xxx,yyy,xxxx,yyyy,dic2):
                    # if flg:
                        tmp.append([xxxx,yyyy, x,y, xx,yy, xxx,yyy])
                        # 0->| 1->- 2->/ 3->\
                        a = x - xx
                        b = y - yy
                        if a != 0 and b != 0:
                            if (a > 0 and b > 0) or (a < 0 and b < 0):
                                if abs(a) == 1 or abs(b) == 1:
                                    node.add((x,y,2))
                                    node.add((xxx,yyy,2))
                                else:
                                    # aa = range(1, a+1) if a >= 0 else range(-1,a-1,-1)
                                    aa = range(1, a) if a >= 0 else range(-1,a,-1)
                                    # bb = range(1, b+1) if b >= 0 else range(-1,b-1,-1)
                                    bb = range(1, b) if b >= 0 else range(-1,b,-1)
                                    for val in zip(aa,bb):
                                        j, k = val
                                        node.add((x-j,y-k,2))
                                        node.add((xxx+j,yyy+k,2))
                            else:
                                if abs(a) == 1 or abs(b) == 1:
                                    node.add((x,y,3))
                                    node.add((xxx,yyy,3))
                                else:
                                    # aa = range(1, a+1) if a >= 0 else range(-1,a-1,-1)
                                    aa = range(1, a) if a >= 0 else range(-1,a,-1)
                                    # bb = range(1, b+1) if b >= 0 else range(-1,b-1,-1)
                                    bb = range(1, b) if b >= 0 else range(-1,b,-1)
                                    for val in zip(aa,bb):
                                        j, k = val
                                        node.add((x-j,y-k,3))
                                        node.add((xxx+j,yyy+k,3))
                        elif a == 0:
                            if abs(a) == 1 or abs(b) == 1:
                                node.add((x,y,0))
                                node.add((xxx,yyy,0))
                            else:
                                # for j in range(1,b+1) if b >= 0 else range(-1,b-1,-1):
                                for j in range(1,b) if b >= 0 else range(-1,b,-1):
                                    node.add((x, y-j, 0))
                                    node.add((xxx, yyy+j, 0))
                        else:
                            if abs(a) == 1 or abs(b) == 1:
                                node.add((x,y,1))
                                node.add((xxx,yyy,1))
                            else:
                                # for j in range(1,a+1) if a >= 0 else range(-1,a-1,-1):
                                for j in range(1,a) if a >= 0 else range(-1,a,-1):
                                    node.add((x-j, y, 1))
                                    node.add((xxx+j, yyy, 1))

                        a = xx - xxx
                        b = yy - yyy
                        if a != 0 and b != 0:
                            if (a > 0 and b > 0) or (a < 0 and b < 0):
                                if abs(a) == 1 or abs(b) == 1:
                                    node.add((xx,yy,2))
                                    node.add((xxxx,yyyy,2))
                                else:
                                    # aa = range(1, a+1) if a >= 0 else range(-1,a-1,-1)
                                    aa = range(1, a) if a >= 0 else range(-1,a,-1)
                                    # bb = range(1, b+1) if b >= 0 else range(-1,b-1,-1)
                                    bb = range(1, b) if b >= 0 else range(-1,b,-1)
                                    for val in zip(aa,bb):
                                        j, k = val
                                        node.add((xx-j,yy-k,2))
                                        node.add((xxxx+j,yyyy+k,2))
                            else:
                                if abs(a) == 1 or abs(b) == 1:
                                    node.add((xx,yy,3))
                                    node.add((xxxx,yyyy,3))
                                else:
                                    # aa = range(1, a+1) if a >= 0 else range(-1,a-1,-1)
                                    aa = range(1, a) if a >= 0 else range(-1,a,-1)
                                    # bb = range(1, b+1) if b >= 0 else range(-1,b-1,-1)
                                    bb = range(1, b) if b >= 0 else range(-1,b,-1)
                                    for val in zip(aa,bb):
                                        j, k = val
                                        node.add((xx-j,yy-k,3))
                                        node.add((xxxx+j,yyyy+k,3))
                        elif a == 0:
                            if abs(a) == 1 or abs(b) == 1:
                                node.add((xx,yy,0))
                                node.add((xxxx,yyyy,0))
                            else:
                                # for j in range(1,b+1) if b >= 0 else range(-1,b-1,-1):
                                for j in range(1,b) if b >= 0 else range(-1,b,-1):
                                    node.add((xx, yy-j, 0))
                                    node.add((xxxx, yyyy+j, 0))
                        else:
                            if abs(a) == 1 or abs(b) == 1:
                                node.add((xx,yy,1))
                                node.add((xxxx,yyyy,1))
                            else:
                                # for j in range(1,a+1) if a >= 0 else range(-1,a-1,-1):
                                for j in range(1,a) if a >= 0 else range(-1,a,-1):
                                    node.add((xx-j, yy, 1))
                                    node.add((xxxx+j, yyyy, 1))
                        if xxxx in dic2:
                            dic2[xxxx].append(yyyy)
                        else:
                            dic2[xxxx] = [yyyy]
                        ls.append([xxxx,yyyy])
                        m += 1
                        # break
                # break
            # break
        if len(ans) < len(tmp):
            ans = tmp
    print(len(ans))
    for val in ans:
        print(*val)
    # print(*sorted(node),sep="\n")

main()
