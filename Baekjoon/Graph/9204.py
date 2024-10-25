from collections import deque


def bfs(start, end):
    q = deque()
    q.append(start)

    dp = [[[] for _ in range(8)] for _ in range(8)]
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    dp[start[0]][start[1]].append(start)

    while q:
        x, y = q.popleft()

        if x == end[0] and y == end[1]:
            return dp[x][y]

        for direction in directions:
            for n in range(1, 8):
                nx = direction[0] * n + x
                ny = direction[1] * n + y

                if 0 <= nx < 8 and 0 <= ny < 8 and len(dp[nx][ny]) == 0:
                    for val in dp[x][y]:
                        dp[nx][ny].append(val)
                    dp[nx][ny].append((nx, ny))
                    q.append((nx, ny))
    return []


test_case = int(input())
code = 65

for _ in range(test_case):
    x1, y1, x2, y2 = input().split()
    x1, y1, x2, y2 = ord(x1) - code, 8 - int(y1), ord(x2) - code, 8 - int(y2)

    result = bfs((y1, x1), (y2, x2))

    if len(result) != 0:
        print(f'{len(result)-1}', end=' ')
        for x, y in result:
            print(f"{chr(y+code)} {8-x}", end=' ')
    else:
        print("Impossible")