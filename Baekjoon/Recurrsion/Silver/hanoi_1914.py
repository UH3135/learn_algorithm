import sys
input = sys.stdin.readline

def hanoi(n, s, m, e):
    if n == 1:
        print(f'{s} {e}')
    else:
        hanoi(n-1, s, e, m)
        print(f'{s} {e}')
        hanoi(n-1, m, s, e)


if __name__ == '__main__':
    n = int(input())
    print(2**n - 1)
    if n <= 20:
        hanoi(n, 1, 2, 3)