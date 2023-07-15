t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    if n % 2 == 0:
        print("YES")
    elif k % 2 == 0:
        print("YES")
    elif (n - 2) % 2 == 0 and (n - 2) > 0:
        print("YES")
    else:
        print("NO")
