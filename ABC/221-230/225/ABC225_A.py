import sys
input = sys.stdin.readline

def main():
    s = input()
    ss = set(s)
    n = len(s) - len(ss)
    if n == 0:
        print(6)
    elif n == 1:
        print(3)
    else:
        print(1)

main()