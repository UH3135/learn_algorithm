def calculate(value, persent):
    return int(value + value * persent * 0.01)


def solution():
    n = 1
    while Y >= n:
        if n >= 5:
            tmp = max(calculate(data[n-1], 5), calculate(data[n-3], 20), calculate(data[n-5], 35))
        elif n >= 3:
            tmp = max(calculate(data[n - 1], 5), calculate(data[n-3], 20))
        else:
            tmp = calculate(data[n-1], 5)
        data.append(tmp)
        n += 1


N, Y = map(int, input().split())
data = [N]
solution()
print(data[Y])
