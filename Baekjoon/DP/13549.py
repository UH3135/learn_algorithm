from collections import deque

def bfs(start, end):
    q = deque([])
    q.append(start)

    visit = [-1] * 1000001
    visit[start] = 0

    move = ["-1", "+1", "*2"]

    while q:
        curr = q.popleft()
        if curr == end:
            return visit[curr]
        for i, v in enumerate(move):
            ne = eval(f"{curr}{v}")
            if 0 <= ne <= 100000:
                if visit[ne] == -1:
                    q.append(ne)
                    if i < 2:
                        visit[ne] = visit[curr] + 1
                    else:
                        visit[ne] = visit[curr]


n, k = map(int, input().split())
print(bfs(n, k))