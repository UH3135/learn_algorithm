import sys
input = sys.stdin.readline


def add_arr(a:list, b:list):
    return [a[0] + b[0], a[1]+b[1]]

def fibo(n):
    if n not in fibo_dict.keys():
        if n == 0:
            fibo_dict[0] = [1, 0]
        elif n == 1:
            fibo_dict[1] = [0, 1]
        else:
            fibo_dict[n] = add_arr(fibo(n-1), fibo(n-2))
    return fibo_dict[n]


if __name__ == '__main__':
    T = int(input())
    fibo_dict = {}
    for _ in range(T):
        n = int(input())
        result = fibo(n)
        for i in result:
            print(i, end=' ')
        print()
