def solution(dp_index, i, j):
    if i == j:
        print('M%d'%(i), end='')
    else:
        k = dp_index[i][j]
        print('(', end='')
        solution(dp_index, i, k)
        solution(dp_index, k+1, j)
        print(')', end='')


T = int(input())  # 테스트 케이스의 수

for _ in range(T):
    length = int(input())
    d = list(map(int, input().split()))

    dp = [[-1 for _ in range(length+1)] for _ in range(length+1)]
    dp_index = [[-1 for _ in range(length+1)] for _ in range(length+1)]

    for i in range(1, length+1):
        dp[i][i] = 0

    for diagonal in range(1, length):
        for i in range(1, length-diagonal+1):
            j = i + diagonal

            min_val = float('inf')
            min_k = 0

            for k in range(i, j):
                value = dp[i][k] + dp[k+1][j] + d[i-1]*d[k]*d[j]
                if min_val > value:
                    min_val = value
                    min_k = k

            dp[i][j] = min_val
            dp_index[i][j] = min_k

    solution(dp_index, 1, length)
    print()
    print(dp[1][length])
