import sys
sys.setrecursionlimit(10**6)
def solution(n):
    if n not in result.keys():
        if n == 1:
            result[1] = 0
            return result[1]

        if n >= 6 and n % 6 == 0:
            result[n] = min(solution(n//3), solution(n//2), solution(n-1)) + 1
        elif n >= 3 and n % 3 == 0:
            result[n] = min(solution(n//3), solution(n-1)) + 1
        elif n >= 2 and n % 2 == 0:
            result[n] = min(solution(n//2), solution(n-1)) + 1
        else:
            result[n] = solution(n-1) + 1

    return result[n]


result = {}
n = int(input())
print(solution(n))