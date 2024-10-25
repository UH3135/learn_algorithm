def fibo_recursion(n):
    if n in result[0].keys():
        return result[0][n]

    if n <= 2:
        result[0][n] = 1
        return 1
    else:
        result[0][n] = (fibo_recursion(n - 1) + fibo_recursion(n - 2))
        return result[0][n]


def fibo_dp(n):
    i = 2
    for _ in range(2):
        result[1].append(1)
    while i < n:
        cnt[1] += 1
        result[1].append(result[1][i-1] + result[1][i-2])
        i += 1
    return result[1][n-1]


N = int(input())

result = [{}, []]
count_dict = {}
cnt = [0, 0]

fibo_recursion(N)
fibo_dp(N)
print(f'{result[1][N-1]} {cnt[1]}')
