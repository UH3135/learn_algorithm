import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append((int(input()), i))

sort_arr = sorted(arr)
result = 0

for i  in range(n):
    if result < sort_arr[i][1] - i:
        result = sort_arr[i][1] - i
print(result+1)