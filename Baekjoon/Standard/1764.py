import sys
input = sys.stdin.readline

a, b = map(int, input().split())
arr = set()
result = set()

for _ in range(a):
    arr.add(input())

for _ in range(b):
    tmp = input()
    if tmp in arr:
        result.add(tmp)

print(len(result))
for i in sorted(result):
    print(i.rstrip())