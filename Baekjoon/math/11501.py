n, k = map(int, input().split())
dp = []

for i in range(n+1):
    if i <= 1:
        dp.append(1)
    else:
        dp.append(dp[i-1]*i)

if k == 0 or n == k:
    print(1)
elif k == 1:
    print(n%10007)
else:
    print((dp[n]//(dp[n-k]*dp[k]))%10007)