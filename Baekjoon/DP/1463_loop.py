def solution(n):
    if n >= 2:
        i = 2
        while i <= n:
            if i >= 6 and i % 6 == 0:
                result.append(min(result[i // 3], result[i // 2], result[i - 1]) + 1)
            elif i >= 3 and i % 3 == 0:
                result.append(min(result[i // 3], result[i - 1]) + 1)
            elif i >= 2 and i % 2 == 0:
                result.append(min(result[i // 2], result[i - 1]) + 1)
            else:
                result.append(result[i - 1] + 1)
            i += 1
    return result[n]

result = [0, 0]

n = int(input())
print(solution(n))