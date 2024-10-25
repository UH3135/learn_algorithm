T = int(input())

dp = [0 for i in range(12)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(T):
    n = int(input())
    if dp[n] != 0:
        print(dp[n])
        continue

    for i in range(n+1):
        if i > 3 and dp[i] == 0:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n])
