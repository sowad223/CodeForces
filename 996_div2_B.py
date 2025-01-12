t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    need = 0
    extra = 0
    for i in range(n):
        if a[i] < b[i]:
            need += b[i] - a[i]
        else:
            extra += a[i] - b[i]

    if extra < need:
        print("NO")
        continue

    if all(x >= y for x, y in zip(a, b)):
        print("YES")
        continue

    surplus = []
    deficit = []
    for i in range(n):
        if a[i] >= b[i]:
            surplus.append(a[i] - b[i])
        else:
            deficit.append(b[i] - a[i])

    surplus.sort(reverse=True)
    deficit.sort()

    ok = False
    i, j = 0, 0
    while i < len(surplus) and j < len(deficit):
        if surplus[i] >= deficit[j]:
            ok = True
            break
        i += 1
        j += 1

    print("YES" if ok else "NO")
