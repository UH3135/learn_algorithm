from collections import deque


def dfs(arr):
    q = deque()
    for i in arr:
        q.append([i])

    while q:
        curr_list = q.popleft()
        if m == len(curr_list):
            q.insert(0, curr_list)
            break
        curr = curr_list[-1]
        for i, v in enumerate(arr):
            tmp = [i for i in curr_list]
            if curr <= v:
                tmp.append(v)
                q.append(tmp)
    return q


n, m = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))

result = dfs(arr)
for i in result:
    for j in i:
        print(j, end=' ')
    print()