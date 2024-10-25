n = int(input())
arr = list(map(int, input().split()))

result = 0
curr = 0

cnt = 0

for i in arr:
    if curr > i:
        cnt += 1
        if cnt > result:
            result = cnt
    else:
        curr = i
        cnt = 0
print(result)