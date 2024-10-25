import sys
input = sys.stdin.readline

def is_palindrome(a:list):
    if len(a) == 0 or len(a) == 1:
        return True
    if a[0] == a[-1]:
        if is_palindrome(a[1:-1]):
            return True
    else:
        return False


if __name__ == '__main__':
    while True:
        s = input().rstrip()
        if s == '0':
            break

        arr = list(s)

        if is_palindrome(arr):
            print('yes')
        else:
            print('no')