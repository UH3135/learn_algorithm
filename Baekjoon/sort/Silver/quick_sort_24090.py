import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def swap(i, j):
    global cnt
    cnt += 1

    arr[i], arr[j] = arr[j], arr[i] # swap

    if cnt == k:
        print(f'{min(arr[i], arr[j])} {max(arr[i], arr[j])}')
        exit()

def partition(start, end):
    tmp = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] <= tmp:
            i += 1
            swap(i, j)

    if (i+1) != end:
        swap(i+1, end)

    return i+1

def quick_sort(start, end):
    if start < end:
        q = partition(start, end)
        quick_sort(start, q-1)
        quick_sort(q+1, end)


if __name__ == '__main__':
    cnt = 0
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    quick_sort(0, n-1)
    if cnt < k:
        print(-1)