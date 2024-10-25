n = int(input())
arr = list(map(int, input().split()))
result = 0
before = 0

for _ in range(n):
    val = min(arr) + before
    arr.remove(min(arr))
    result += val
    before = val
print(result)