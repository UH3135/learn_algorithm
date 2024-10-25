#변수 정리
n = int(input())
arr = []

dp = []

for _ in range(n):
    arr.append(int(input()))

for i,v in enumerate(arr):
    if i == 0:
        dp.append(v)
    else:
        dp.append(max(dp[i-1], v))
print(dp[-1])