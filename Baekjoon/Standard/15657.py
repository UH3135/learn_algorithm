from collections import deque

def solution(n, m, arr):
    q = deque()
    for i in arr:
        q.append([i])

    result = []

    while q:
        curr = q.popleft()
        if len(curr) == m:
            result.append(curr)
            continue

        val = [j for j in curr]

        for i in arr:
            if i >= curr[-1]:
                q.append(val + [i])

    return result

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sorted(arr)

for ar in solution(n, m, sorted(arr)):
    for num in ar:
        print(num, end=' ')
    print()

