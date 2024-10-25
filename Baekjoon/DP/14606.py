def solution(n):
    if n == 1: return

    end = n//2 + 1 if n%2 == 0 else n//2 + 2
    value = 0
    divide = [0, 0]

    for i in range(1, end):
        if value < i*(n-i):
            value = i*(n-i)
            divide[0], divide[1] = i, (n-i)

    global result
    result += value

    solution(divide[0])
    solution(divide[1])


result = 0
num = int(input())

solution(num)
print(result)