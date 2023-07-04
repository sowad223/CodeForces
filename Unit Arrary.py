t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    pos = sum(1 for i in arr if i > 0)
    neg = n - pos

    if pos >= neg:
        if neg % 2 == 0:
            print(0)
        else:
            print(1)
    else:
        half = n // 2
        dif = neg - half
        if half % 2 != 0:
            dif += 1
        print(dif)