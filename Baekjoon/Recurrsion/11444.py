import sys
input = sys.stdin.readline

p = 1000000
a = [[1, 1], [1, 0]]

def pow(a, b):
    result = [
        [(a[0][0]*b[0][0] + a[0][1]*b[1][0])%p, (a[0][0]*b[0][1] + a[0][1]*b[1][1])%p],
        [(a[1][0]*b[0][0] + a[1][1]*b[1][0])%p, (a[1][0]*b[0][1] + a[1][1]*b[1][1])%p]
    ]
    return result


def fibo(n):
    if n == 0:
        return [[1, 0], [0, 1]]
    if n == 1:
        return a

    tmp = fibo(n//2)

    if n%2 == 1:
        return pow(pow(tmp, tmp), a)
    else:
        return pow(tmp, tmp)


n = int(input())
print(fibo(n)[1][0])