"""
f(n) = f(n-1) + f(n-5) (n >= 5)
if n <= 2 : 1
if 2 < n < 5 : 2
"""
T = int(input())
dp = []

for _ in range(T):
    n = int(input())

    for i in range(n):
        if len(dp) > i:
            continue
        if i <= 2:
            dp.append(1)
        elif i < 5:
            dp.append(2)
        else:
            dp.append(dp[i-1] + dp[i-5])
    print(dp[n-1])