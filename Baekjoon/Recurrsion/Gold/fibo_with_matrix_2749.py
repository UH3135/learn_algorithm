import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dot(x:list, y:list):
    result = []
    for i in range(0, 2):
        tmp = []
        for j in range(0, 2):
            tmp.append(x[i][0] * y[0][j] + x[i][1] * y[1][j])
        result.append(tmp)
    return result

def fibo(n):
    if n not in memo.keys():
        if n%2 == 0:
            memo[n] = dot(fibo(n//2), fibo(n//2))
        else:
            memo[n] = dot(fibo(n//2), fibo(n//2+1))
    return memo[n]


if __name__ == '__main__':
    n = int(input())
    memo = {1: [[1, 1], [1, 0]]}
    print(fibo(n)[0][1]%1000000)
