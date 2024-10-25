def solution(arr, s, n, c):
    if n == c:
        print(s)
        return
    elif c == 0:
        for i in arr:
            solution(arr, i, n, c+1)
    else:
        for i in arr:
            solution(arr, s + " " + i, n, c+1)


n, m = map(int, input().split())
arr = [str(i) for i in range(1, n+1)]

solution(arr, "", m, 0)

