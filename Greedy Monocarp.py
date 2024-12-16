t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    s = 0
    for i in a:
        s += i
        if s > k:
            s -= i
            break
    print(k-s)