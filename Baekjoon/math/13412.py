def GCD(a, b):
    big = max(a, b)
    small = min(a, b)

    while True:
        tmp = big % small
        if tmp == 0:
            val = small
            break
        else:
            if tmp > small:
                big = tmp
            else:
                big, small = small, tmp
    return val


T = int(input())

for _ in range(T):
    num = int(input())
    arr = []
    for i in range(1, num+1):
        if num % i == 0:
            if num//i < i:
                break
            arr.append((i, num//i))

    result = 0

    for x, y in arr:
        if GCD(x, y) == 1:
            result += 1
    print(result)