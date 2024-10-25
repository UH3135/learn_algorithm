import sys
input = sys.stdin.readline

def check(n):
    for i in range(n):
        if stack[n] == stack[i] or abs(stack[n]-stack[i]) == n-i:
            return False
    return True


def solution(curr, n):
    if curr == n:
        global cnt
        cnt += 1
    else:
        for i in range(n):
            stack[curr] = i
            if check(curr):
                stack[curr] = i
                solution(curr+1, n)
                stack[curr] = -1


n = int(input())
stack = [-1] * n
cnt = 0
solution(0, n)
print(cnt)