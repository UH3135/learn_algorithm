n = int(input())

dp = [0 for _ in range(n)]

for i in range(n):
    if i < 3 and i == 0 or i == 2:
        dp[i] = 1
    elif i == 1:
        dp[i] = 2
    else:
        dp[i] = min(dp[i-1], dp[i-3]) + 1

if dp[n-1] % 2 == 0:
    print('SK')
else:
    print('CY')
