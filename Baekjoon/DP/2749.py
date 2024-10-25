def dot(A, B):
    result = [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
    ]
    return result


def fibo(n):
    a = [[1, 1],[1, 0]]
    ans = [[1, 0], [0, 1]]
    i = n
    while i > 0:
        if i%2 == 1:
            ans = dot(ans, a)
        a = dot(a, a)
        i = i//2
    return ans[0][1]


n = int(input())
result = fibo(n)
print(result%1000000)