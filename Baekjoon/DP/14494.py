def solution(n, m):
    for row in range(m):
        for column in range(n):
            if row == 0:
                result[0][column] = 1
            elif column == 0:
                result[row][0] = 1
            else:
                result[row][column] = (result[row-1][column] + result[row][column-1] + result[row-1][column-1])%1000000007


n, m = map(int, input().split())
result = [[0 for _ in range(n)] for _ in range(m)]
solution(n, m)
print(result[m-1][n-1])