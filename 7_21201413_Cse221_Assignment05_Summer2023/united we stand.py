t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    flag = True
    for i in range(n):
        if arr[i] != arr[-1]:
            flag = False
            break

    if flag:
        print()
        print(-1)
    else:
        arr.sort()
        b=[]
        c =[]

        m = 0
        for i in range(n - 1, -1, -1):
            if arr[i] ==arr[0]:
                b.insert(0, str(arr[i]))
                m+= 1
            else:
                c.insert(0, str(arr[i]))

        c1= n -m
        print(m,c1)

        print(" ".join(b))
        print(" ".join(c))