def next_permu(arr, length):
    for i, v in enumerate(list(reversed(arr))):
        curr_index = length-i-1
        if curr_index == 0:
            continue

        next_index = curr_index - 1
        if arr[next_index] < v:
            # 기준 좌 우를 구분
            left_arr = arr[:curr_index]
            right_arr = arr[curr_index:]

            standard = left_arr[-1]

            for j, v2 in enumerate(list(reversed(right_arr))):
                if standard < v2:
                    left_arr[-1], right_arr[j] = right_arr[j], left_arr[-1]
                    result = left_arr+sorted(right_arr)
                    return result


arr = [1, 3, 2]
print(next_permu(arr, 3))