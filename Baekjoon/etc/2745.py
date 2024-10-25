N, B = input().split()
B = int(B)

result = 0

key_list = [str(i) for i in range(1, 10)] + ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
value_list = [i for i in range(1, 36)]

count_dict = dict(zip(key_list, value_list))

for i in range(len(N)):
    result += count_dict[N[i]]*B**i

print(result)