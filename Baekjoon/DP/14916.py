import sys
sys.setrecursionlimit(10**5)
def get_value(num1, num2):
    if num1 == -1 or num2 == -1:
        if num1 != -1:
            return num1
        elif num2 != -1:
            return num2
        else:
            return -2  # solution에서 값을 -1로 설정 할 수 있도록 하기 위해서

    if num1 <= num2:
        return num1
    else:
        return num2


def solution(n):
    if n not in d.keys():
        d[n] = get_value(solution(n-2), solution(n-5)) + 1
    return d[n]



n = int(input())
d = {1: -1, 2: 1, 3: -1, 4: 2, 5: 1}

solution(n)
print(d[n])
