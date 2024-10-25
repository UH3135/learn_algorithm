def dfs():
	if len(stack) == k:
		result.add("".join(map(str, stack)))
		return
	else:
		for i, v in enumerate(arr):
			if chk[i]:
				stack.append(v)
				chk[i] = False

				dfs()

				stack.pop()
				chk[i] = True


n = int(input())
k = int(input())

arr = []
stack = []
chk = [True] * n
result = set()

for _ in range(n):
	arr.append(int(input()))
dfs()
print(len(result))
