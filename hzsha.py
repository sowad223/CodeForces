
t = int(input())

for _ in range(t):
        r = {}
        for i in range(8):
            row = input().strip()
            r[i] = "".join([i for i in row if i != '.'])

        k = "".join(r.values())
        print(k)

