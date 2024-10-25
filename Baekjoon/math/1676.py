def factorial(n):
    val = 1
    for i in range(1, n+1):
        val *= i
    return val


n = int(input())
dp = [0 for _ in range(n+1)]

num = list(str(factorial(n)))[::-1]
cnt = 0
for i in num:
    if i != "0":
        print(cnt)
        break
    else:
        cnt += 1