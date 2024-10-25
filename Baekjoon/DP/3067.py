T = int(input())

for _ in range(T):
    length = int(input())
    coins = list(map(int, input().split()))
    count = int(input())

    dp = [0 for _ in range(count+1)]

    for coin in coins:
        for num in range(1, count+1):
            if num == coin:
                dp[num] += 1
            if num > coin:
                dp[num] += dp[num-coin]

    print(dp[-1])