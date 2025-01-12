
t = int(input().strip())


for i in range(t):

    x = input().strip().split()
    n = int(x[0])
    a = int(x[1])
    b = int(x[2])


    d = abs(a - b)

    if d % 2 == 0:
        print("YES")
    else:
        print("NO")
