def solution(arr):
    for i, v in enumerate(arr):
        if i == 0:
            continue
        if arr[i-1] > v:
            return False
    return True

arr = list(map(int, input().split()))

if solution(arr):
    print("Good")
else:
    print("Bad")