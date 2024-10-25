from collections import deque


def bfs(start, end):
    upper = 100000
    lower = 0

    q = deque()
    q.append(start)
    move = ["+1", "-1", "*2"]
    dp = [-1 for _ in range(100001)]
    dp[start] = 0

    while q:
        loc = q.popleft()

        if loc == end:
            return dp[loc]

        for oper in move:
            nloc = eval(str(loc)+oper)
            if lower <= nloc <= upper and dp[nloc] == -1:
                q.append(nloc)
                dp[nloc] = dp[loc] + 1
    return -1

arr = list(map(int, input().split()))
print(bfs(arr[0], arr[1]))