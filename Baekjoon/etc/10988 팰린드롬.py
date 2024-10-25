"""
문제: 10988 팰린드롬인지 확인하기
"""

word = input()

for i in range(len(word)//2):
    if word[0] == word[-1]:
        word = word[1:-1]
    else:
        print(0)
        break

if len(word) <= 1:    
    print(1)