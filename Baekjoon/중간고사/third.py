import sys
input = sys.stdin.readline

def get_team(arr, n):
    i = 0
    mem_list = []
    while i < n and len(mem_list) != n:
        mem_list.append(i)
        j = i
        while True:
            if (arr[j]-1) in mem_list:
                break
            mem_list.append(arr[j]-1)
            j = arr[j]-1
        i += 1
    i += n - len(mem_list)
    return i


T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    n = arr[0]
    arr = arr[1:]

    print(get_team(arr, n))

