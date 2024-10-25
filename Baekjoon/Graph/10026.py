from collections import deque


def bfs(arr, dp):
    q = deque()
    


n = int(input())
arr = []
dp = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    arr.append(list(str(input())))

blind_arr = arr.copy()
for i, ar in enumerate(blind_arr):
    for j, v in enumerate(blind_arr):
        if v == "G":
            blind_arr[i][j] = "R"

print(arr)
print(blind_arr)