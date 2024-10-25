n = int(input())
words = ["baby", "sukhwan", "tururu", "turu",
"very", "cute", "tururu", "turu",
"in", "bed", "tururu", "turu",
"baby", "sukhwan"
]

i = n % 14 - 1 
k = n // 14   
tu_indexs = [2, 3, 6, 7, 10, 11]
tu_long_indexs = [2, 6, 10]

if i in tu_indexs:
    if k >= 3 and i in tu_long_indexs:
        print(f"tu+ru*{k+2}")
    elif k >= 4 and i not in tu_long_indexs:
        print(f"tu+ru*{k+1}")
    else:
        print(words[i] + "ru"*k)
else:
    print(words[i])