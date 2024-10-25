n = int(input())

dp = [0 for _ in range(n+1)]

for i in range(n+1):
    if i == 0:
        dp[0] = 1
    else:
        tmp = 0
        for j in range(n+1):
            tmp += dp[j]*dp[i-(j+1)]
        dp[i] = tmp

print(dp[n])