def solution(a, n):
    result = a
    length = n
    while length > 2:
        t = []

        for i in range(length-1):
            t.append((result[i] + result[i+1])%10)

        result = t
        length -= 1
    return result


arr_input = []
alpabet = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
tmp = []

for _ in range(2):
    tmp.append([alpabet[n-65] for n in list(map(ord, list(input())))])

for i in range(len(tmp[0])):
    arr_input.append(tmp[0][i])
    arr_input.append(tmp[1][i])

print(''.join(map(str, solution(arr_input, len(arr_input)))))
