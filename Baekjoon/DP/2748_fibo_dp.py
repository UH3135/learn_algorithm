def fibo(n):
    if n not in dp:
        if n == 0 or n == 1:
            dp[n] = n
        else:
            dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]



dp = {}
n = int(input())
print(fibo(n))