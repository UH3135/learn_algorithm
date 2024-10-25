def LCS(arr1, arr2):
    dp = [[[] for _ in range(len(arr1)+1)] for _ in range(len(arr2)+1)]

    for i, v1 in enumerate(arr2):
        for j, v2 in enumerate(arr1):
            if v1 == v2:
                value = dp[i][j] + [v1]
            elif len(dp[i+1][j]) > len(dp[i][j+1]):
                value = dp[i+1][j]
            else:
                value = dp[i][j+1]

            dp[i+1][j+1] = value

    return dp[-1][-1]

a = list(input())
b = list(input())

result = LCS(a, b)

print(len(result))
print("".join(result))