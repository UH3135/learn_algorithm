import itertools


def condition(a, n):
    for i, v in enumerate(a):
        if i != n-1 and a[i+1] < v:
            return False
    return True

def get_subseq(a, n):
    subseq = list(itertools.permutations(a))
    del_seq = []
    for i in subseq:
        if not condition(i, n):
            del_seq.append(i)

    for i in del_seq:
        subseq.remove(i)

    return subseq

n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
