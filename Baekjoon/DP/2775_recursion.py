def solution(k, n):
    if dp[k][n] == 0:
        if k == 0:
            value = n
        elif n == 1:
            value = 1
        else:
            value = solution(k, n-1) + solution(k-1, n)
        dp[k][n] = value
    return dp[k][n]

T = int(input())
dp = [[0 for _ in range(15)] for _ in range(15)]
for _ in range(T):
    k = int(input())
    n = int(input())
    print(solution(k, n))

