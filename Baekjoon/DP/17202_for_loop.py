def solution(a):
    arr = a.copy()
    while len(arr) > 2 and a != [1, 0, 0]:
        for i, v in enumerate(a[:-1]):
            arr.append((v+a[i+1])%10)
    return arr


a = list(map(int, input()))
b = list(map(int, input()))

result = []
for a, b in zip(a, b):
    result.append(a)
    result.append(b)

print(solution(result))
