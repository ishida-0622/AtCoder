import sys
input = sys.stdin.readline

def main():
    n = int(input())
    lst = [list(map(int, input().split(' '))) for _ in range(n - 1)]
    for i in range(1,n + 1):
        flag = True
        for j in range(n - 1):
            if i not in lst[j]:
                flag = False
                break
        if flag:
            break
    if flag:
        print('Yes')
    else:
        print('No')
main()