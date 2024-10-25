def solution():
    for w in range(weight+1):
        for i in range(n+1):
            if w == 0 or i == 0:
                continue
            if weights[i-1] > w:
                dp[w][i] = dp[w][i-1]
            else:
                dp[w][i] = max(dp[w][i-1], values[i-1] + dp[w-weights[i-1]][i-1])

    return 0


n, weight = map(int, input().split())

weights = []
values = []

dp = [[0]*(n+1) for _ in range(weight+1)]

for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

solution()
# for i in dp:
#     for j in i:
#         print(j, end=' ')
#     print()
print(dp[-1][-1])
