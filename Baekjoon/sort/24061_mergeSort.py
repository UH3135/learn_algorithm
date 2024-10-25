import sys
input = sys.stdin.readline


def merge(start, mid, end):
    global cnt
    tmp = []

    i = start
    j = mid+1

    if cnt == k:
        return None

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    while i <= mid:
        tmp.append(arr[i])
        i += 1

    while j <= end:
        tmp.append(arr[j])
        j += 1

    i = start
    for x in tmp:
        arr[i] = x
        i += 1
        cnt += 1
        if cnt == k:
            return None



def merge_sort(start, end):
    if start < end and cnt != k:
        mid = (start+end) // 2
        merge_sort(start, mid)
        merge_sort(mid+1, end)
        merge(start, mid, end)


if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0

    merge_sort(0, n-1)

    if cnt < k:
        print(-1)
    else:
        for i in arr:
            print(i, end=' ')
