def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

num = int(input())
arr = list(str(factorial(num)))

for i in arr[::-1]:
    if i != "0":
        print(i)
        break