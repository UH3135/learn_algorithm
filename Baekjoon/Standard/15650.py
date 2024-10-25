import itertools


n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]

result = list(itertools.combinations(arr, m))

for i in result:
    for j in i:
        print(j, end=' ')
    print()
