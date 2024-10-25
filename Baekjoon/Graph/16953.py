from collections import deque


def bfs(start, end):
    q = deque()
    q.append(start)
    dp = [0 for _ in range(end+1)]

    while q:
        now = q.popleft()

        for i in range(2):
            if i == 0:
                num = int(str(now) + "1")
            elif i == 1:
                num = now * 2

            if dp[num] == 0:
                q.append(num)
                dp[num] = dp[now] + 1

                if num == end:
                    return dp[num]



a, b = map(int, input().split())
print(bfs(a, b))