def next_permutation(arr):
    tmp = [i for i in arr]
    length = len(tmp)
    for i in range(length-1, 0, -1):
        if tmp[i] > tmp[i-1]:

            for j in range(length-1, 0, -1):
                if tmp[j] > tmp[i-1]:
                    tmp[i-1], tmp[j] = tmp[j], tmp[i-1]
                    break

            tmp[i:] = sorted(tmp[i:])
            break
    return tmp


n = int(input())
arr = list(map(int, input().split()))

result = next_permutation(arr)

if result == arr or n == 1:
    print(-1)
else:
    for i in result:
        print(i, end=" ")