def solution(x, y):
    row = len(x)
    column = len(y)
    if row == 0 or column == 0:
        return 0
    if memo[row][column] != -1:
        return memo[row][column]

    if x[-1] == y[-1]:
        memo[row][column] = solution(x[:-1], y[:-1]) + 1
    else:
        memo[row][column] = max(solution(x[:-1], y), solution(x, y[:-1]))

    return memo[row][column]


T = int(input())

for _ in range(T):
    X, Y = [list(word) for word in input().split()]
    memo = [[-1 for _ in range(len(Y) + 1)] for _ in range(len(X) + 1)]
    print(solution(X, Y))
