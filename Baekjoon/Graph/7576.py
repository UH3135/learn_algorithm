from collections import deque


def bfs(arr, dp):
    q = deque()
    for i in dp:
        q.append(i)
    move_x = [0, 0, 1, -1]
    move_y = [1, -1, 0, 0]

    while q:
        x, y = q.popleft()

        for ax, ay in zip(move_x, move_y):
            nx = x + ax
            ny = y + ay
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                q.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1



    return 0


M, N = map(int, input().split())
arr = []
dp = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            dp.append((i, j))

bfs(arr, dp)

result = 0
for i in arr:
    for j in i:
        if j == 0:
            result = -1
        if j > result and result != -1:
            result = j-1
print(result)
