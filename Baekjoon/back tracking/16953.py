from collections import deque


def oper(n):
    return int(str(n) + "1")


def back_tracking(n, answer):
    q = deque()
    q.append([n])

    result = 1

    while True:
        curr_list = q.pop()
        tmp = []
        for curr in curr_list:
            if curr == answer:
                return result

            if curr*2 <= answer:
                tmp.append(curr*2)
            if oper(curr) <= answer:
                tmp.append(oper(curr))
        if len(tmp) == 0:
            break
        q.append(tmp)
        result += 1
    return -1


a, b = map(int, input().split())
print(back_tracking(a, b))
