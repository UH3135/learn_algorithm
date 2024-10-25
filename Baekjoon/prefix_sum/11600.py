import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = []
dp = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i, row in enumerate(arr):
    for j, value in enumerate(row):
        if i == 0 and j == 0:
            dp[i][j] = value
        elif i == 0:
            dp[i][j] = value + dp[i][j-1]
        elif j == 0:
            dp[i][j] = value + dp[i-1][j]
        else:
            dp[i][j] = value + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for _ in range(m): # Test case
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1

    if x1 == 0 and y1 == 0:
        print(dp[x2][y2])
    elif x1 == 0:
        print(dp[x2][y2] - dp[x2][y1-1])
    elif y1 == 0:
        print(dp[x2][y2] - dp[x1-1][y2])
    else:
        print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])
