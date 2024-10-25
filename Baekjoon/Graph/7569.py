from collections import deque


def bfs(arr, starts):
    q = deque()
    result = 0
    move_x = [0, 0, 0, 0, 1, -1]
    move_y = [0, 0, 1, -1, 0, 0]
    move_z = [1, -1, 0, 0, 0, 0]

    for start in starts:
        q.append(start)
        result = 1
    
    while q:
        x, y, z = q.popleft()

        for ax, ay, az in zip(move_x, move_y, move_z):
            nx = x + ax
            ny = y + ay
            nz = z + az
            
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and arr[nz][ny][nx] == 0:
                q.append((nx, ny, nz))
                arr[nz][ny][nx] = arr[z][y][x] + 1
                if result < arr[nz][ny][nx]:
                    result = arr[nz][ny][nx]

    for i in arr:
        for j in i:
            for k in j:
                if k == 0:
                    return -1
    return result - 1


M, N, H = map(int, input().split())

arr = []
starts = []
for _ in range(H):
    tmp = []
    for _ in range(N):
        tmp.append(list(map(int, input().split())))
    arr.append(tmp)

for i, arr_v in enumerate(arr):
    for j, v in enumerate(arr_v):
        for k, c in enumerate(v):
            if c == 1:
                starts.append((k, j, i))

print(bfs(arr, starts))
