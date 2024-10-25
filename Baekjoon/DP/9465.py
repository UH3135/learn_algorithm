def solution(n):
    dp = [[0] * n for _ in range(2)]
    

    for i in range(n):
        if i == 0:
            dp[0][i] = arr[0][i]
            dp[1][i] = arr[1][i]
        elif i == 1:
            dp[0][i] = arr[0][i] + arr[1][0]
            dp[1][i] = arr[1][i] + arr[0][0]
        else:
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + arr[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + arr[1][i]
    return dp
            


T = int(input())

for _ in range(T):
    n = int(input())
    arr = []

    for i in range(2):
        arr.append(list(map(int, input().split())))

    result = solution(n)

    print(max(result[0][-1], result[1][-1]))
