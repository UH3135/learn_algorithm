import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_min_max(arr, s, e):
    global cnt
    cnt += 1

    value = []

    if e-s == 0:
        return [arr[s], arr[s]]
    elif e-s == 1:
        return [min(arr[s:e+1]), max(arr[s:e+1])]
    else:
        m = (s+e)//2
        minmax1 = find_min_max(arr, s, m)
        minmax2 = find_min_max(arr, m+1, e)

        if minmax1[0] < minmax2[0]:
            value.append(minmax1[0])
        else:
            value.append(minmax2[0])

        if minmax1[1] < minmax2[1]:
            value.append(minmax2[1])
        else:
            value.append(minmax1[1])
    return value

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        cnt = 0
        arr = list(map(int, input().split()))
        n = arr[0]
        arr = arr[1:]

        result = find_min_max(arr, 0, n-1)
        print(f'{result[1]} {result[0]} {cnt}')
