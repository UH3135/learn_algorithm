class Set():
    def __init__(self):
        self.data = []

    def add(self, n):
        if n in self.data:
            return
        self.data.append(n)

    def remove(self, n):
        if n in self.data:
            self.data.remove(n)


    def check(self, n):
        if n in self.data:
            print(1)
        else:
            print(0)


    def toggle(self, n):
        if n in self.data:
            self.data.remove(n)
        else:
            self.data.append(n)


m = int(input())
main = Set()

for _ in range(m):
    tmp = list(input().split())
    cmd = tmp[0]

    if cmd == 'all':
        main.data = [i for i in range(1, 21)]
    elif cmd == 'empty':
        main.data = []
    else:
        num = int(tmp[1])

        if cmd == 'add':
            main.add(num)
        elif cmd == 'remove':
            main.remove(num)
        elif cmd == 'check':
            main.check(num)
        elif cmd == 'toggle':
            main.toggle(num)
        else:
            print("Error")
