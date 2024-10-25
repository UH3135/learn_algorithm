def quick_sort(start, end):
    # 만약 시작과 끝이 동일하다면 재귀 멈추기
    if start == end:
        return
    pivot = start
    low = start + 1
    high = end

    # 스타트와 엔드의 값이 교차될 때 까지 반복 end < start
    while high >= low:
        if arr[low] < arr[pivot]:  # 만약 스타트가 피벗보다 작으면 오른쪽으로 옮기기
            low += 1
        if arr[high] > arr[pivot]:  # 만약 엔드가 피벗보다 크면 왼쪽으로 옮기기
            high -= 1
        if arr[high] < arr[pivot] < arr[low]:    # 만약 스타트가 피벗보다 크고 엔드가 피벗보다 작으면 둘을 스왑
            arr[high], arr[low] = arr[low], arr[high]
    if arr[pivot] > arr[high]:
        arr[high+1], arr[pivot] = arr[pivot], arr[high+1]
    else:
        arr[high - 1], arr[pivot] = arr[pivot], arr[high - 1]

    # 피벗을 기준으로 양 방향 arr를 퀵정렬
    quick_sort(start, pivot-1)
    quick_sort(pivot+1, end)



n, k = map(int, input().split())
arr = list(map(int, input().split()))

quick_sort(0, n-1)
print(arr)