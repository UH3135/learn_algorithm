from decimal import Decimal


def solution(a):
    dp =[]
    dp.append(a[0])
    for i in a[1:]:
        dp.append(max(i, i*dp[a.index(i)-1]))
    return dp


N = int(input())
a = []

for _ in range(N):
    a.append(Decimal(input()))
print('%0.3f' % max(solution(a)))
