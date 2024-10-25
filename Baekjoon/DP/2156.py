n = int(input())
arr = [0]
dp = [0 for _ in range(n+1)]
for _ in range(n):
    arr.append(int(input()))

for i, v in enumerate(arr):
    if i < 2:
        dp[i] = v
    elif i == 2:
        dp[i] = v + dp[i-1]
    else:
        dp[i] = max(v + arr[i-1]+ dp[i-3], v + dp[i-2], dp[i-1])
print(dp[-1])