# from collections import deque
# 점화식 : f(0) = arr[0][0]
# f[x][y] = max(dp[x-1][y], dp[x-1][y+1]) + arr[n] 단, n != 0 or -1
# 0 or -1 = f[x][y] = f[x][0] or f[x][-1]
#
# def dp(arr, start, end):
#

n = int(input())
arr = []
dp = []

for i in range(1, n+1):
    arr.append(list(map(int, input().split())))
    dp.append([0 for j in range(i)])

for row in range(n):
    for column in range(row+1):
        if row == 0:
            dp[row][column] = arr[0][0]
            continue
        if column == 0:
            dp[row][column] = arr[row][column] + dp[row-1][0]
        elif column == row:
            dp[row][column] = arr[row][-1] + dp[row-1][-1]
        else:
            dp[row][column] = max(dp[row-1][column], dp[row-1][column-1]) + arr[row][column]
print(max(dp[-1]))
