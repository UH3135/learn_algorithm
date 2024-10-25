from collections import deque


def bfs(arr):
    q = deque()
    dp = [[0 for _ in range(N)] for _ in range(M)]

    for i, row in enumerate(arr):
        for j, val in enumerate(row):
            if val == 2:
                q.append((i, j))
                dp[i][j] = 2
            elif val == 1:
                dp[i][j] = 1

    move_x = [0, 0, -1, 1]
    move_y = [1, -1, 0, 0]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(move_x, move_y):
            nx = x + dx
            ny = x + dy

            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0 and dp[nx][ny] == 0:
                q.append((nx, ny))
                dp[nx][ny] = 1
    cnt = 0

    for row in arr:
        cnt += row.count(0)
    return cnt


N, M = map(int, input().split())
arr = []
starts = []
for _ in range(M):
    arr.append(list(map(int, input().split())))

print(bfs(arr))

