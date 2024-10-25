import sys


def swap(a, b):
    arr[a], arr[b] = arr[b], arr[a]

    global count
    count += 1
    if count == k:
        for s in arr:
            print(s, end=' ')
        sys.exit()


def partition(start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end-1):
        if arr[j] <= pivot:
            i += 1
            swap(i, j)
    if i+1 != end:
        swap(i+1, end)

    return i+1


def quick_sort(start, end):
    if start < end:
        p = partition(start, end)
        quick_sort(start, p-1)
        quick_sort(p+1, end)


n, k = map(int, input().split())
count = 0
arr = list(map(int, input().split()))

quick_sort(0, n-1)
print(-1)