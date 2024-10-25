def solution(num):
    if num >= len(result):
        i = 3
        while i <= num:
            result.append(min(result[i-3], result[i-1]) + 1)
            i += 1
    return result[num]

result = [0, 1, 2]

n = int(input())

if solution(n)%2 == 0:
    print('CY')
else:
    print('SK')