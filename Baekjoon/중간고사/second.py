import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def get_length(a, n):
    start = 0
    result = 1
    for i in range(n-1):
        if a[i] > a[i+1]:
            tmp = (i-start)+1
            if tmp > result:
                result = tmp
            start = i+1
        if i+1 == n-1 and a[i] == a[i+1]:
            tmp = (i+1 - start) + 1
            if tmp > result:
                result = tmp

    return result

T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    n = arr[0]
    arr = arr[1:]

    print(get_length(arr, n))