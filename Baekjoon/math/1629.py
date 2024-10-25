import sys
input = sys.stdin.readline

def pow(num, cnt):
    if cnt == 1:
        return a%c

    tmp = pow(num, cnt//2)

    if cnt%2:
        return (tmp * tmp * a) % c
    else:
        return (tmp * tmp) % c


a, b, c = map(int, input().split())
print(pow(a, b))
