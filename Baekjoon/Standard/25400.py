n = int(input())
arr = list(map(int, input().split()))

cnt = 0
curr = 1

for i in arr:
    if i == curr:
        curr += 1
    else:
        cnt += 1

print(cnt)
