def check_nine(n):
    cnt = 0
    for i in str(n):
        if i == '9':
           cnt += 1

    if cnt == 0:
        return [False, cnt]
    else:
        return [True, cnt]


# 입력
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 변수 초기화
all_counter = 0
column_counter = [0] * m

max_value = 0  # 현재 최댓값

for row in range(n):  # 행 반복
    row_counter = 0  # 행 카운터 초기화
    for column, value in enumerate(arr[row]):  # 열 반복
        boolean, count = check_nine(value)
        if boolean:  # 만약 값이 9 이면 행, 열, 전체 카운터 +1
            all_counter += count
            column_counter[column] += count
            row_counter += count
    max_value = max(max_value, row_counter)  # 만약 현재 최대 갯수 보다 행카운터 값이 크면 최신화

print(all_counter - max(max_value, max(column_counter)))  # 결과는 전체 - (최대 갯수와 열 카운터 Max 값)