from itertools import permutations

n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = sorted(list(permutations(arr, m)))

for a in result:
    for i in a:
        print(i, end=' ')
    print()