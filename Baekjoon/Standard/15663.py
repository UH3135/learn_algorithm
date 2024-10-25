import itertools


n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = sorted(set(itertools.permutations(arr, m)))

for i in result:
    for j in i:
        print(j, end=' ')
    print()