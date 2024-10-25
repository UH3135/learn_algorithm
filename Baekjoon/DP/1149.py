N = int(input())
arr = []
dp = [[None for _ in range(3)] for _ in range(N)] # 0번은 RGB (0,1,2), 1번 인덱스는 value

# input
for _ in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
dp[0][2] = arr[0][2]

for i in range(1, N):
    for j in range(3):
        another = [x for x in range(3) if x != j]
        dp[i][j] = min(dp[i-1][another[0]] + arr[i][j], dp[i-1][another[1]] + arr[i][j])

print(min(dp[N-1]))
