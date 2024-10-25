from collections import deque

n = int(input())
x, y = map(int, input().split())

visit = [[0 for _ in range(n)] for _ in range(n)]
visit[n-y][x-1] = 1

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

q = deque()
q.append((visit, 0)) # 두번째 인덱스는 이동 횟수

# for i in visit:
#     for j in i:
#         print(j, end=' ')
#     print()

