import sys

n, k = map(int, input().split())  # range, count
arr = list(map(int, input().split()))

cnt = 0

for last in range(n-1, -1, -1):
    max_val = 0
    max_index = -1
    for i, v in enumerate(arr[:last+1]):
        if v > max_val:
            max_val = v
            max_index = i
    if max_index != last:
        arr[max_index], arr[last] = arr[last], arr[max_index]
        cnt += 1
        if cnt == k:
            print(arr[max_index], arr[last])
            sys.exit()
print(-1)
