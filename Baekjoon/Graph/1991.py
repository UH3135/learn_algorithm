def pre_order(curr):
    if curr == ".":
        return

    print(curr, end='')
    pre_order(tree[curr][0])
    pre_order(tree[curr][1])

def inorder(curr):
    if curr == ".":
        return

    inorder(tree[curr][0])
    print(curr, end='')
    inorder(tree[curr][1])

def postorder(curr):
    if curr == ".":
        return

    postorder(tree[curr][0])
    postorder(tree[curr][1])
    print(curr, end='')

n = int(input())
tree = {}

for _ in range(n):
    key, value1, value2 = map(str, input().split())
    tree[key] = [value1, value2]

pre_order('A')
print()
inorder('A')
print()
postorder('A')
print()
