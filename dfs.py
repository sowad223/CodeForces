t = int(input())
for _ in range(t):
    n = int(input())
    m = 0
    k = 0
    winner = False
    for i in range(1, n + 1):
        words, quality = map(int, input().split())
        if words <= 10 and quality >m:
            m,k = quality,i
            winner = True
    if winner:
        print(k)


