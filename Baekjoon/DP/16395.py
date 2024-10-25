def solution(n):
    row = 2
    while n > row:
        tmp = []
        for column in range(row+1):
            if column == 0 or column == row:
                tmp.append(1)
            else:
                tmp.append(result[row-1][column] + result[row-1][column-1])
        result.append(tmp)
        row += 1


result = [[1], [1, 1]]
n, k = map(int, input().split())

solution(n)
print(result[n-1][k-1])