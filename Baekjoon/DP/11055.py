n = int(input())
arr = list(map(int, input().split()))

dp = [-1] * n
dp[0] = arr[0]

for i in range(n):
    dp[i] = arr[i]
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], arr[i] + dp[j])

print(max(dp))