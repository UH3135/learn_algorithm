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


solution(["1", "2"], "", 2, 0)