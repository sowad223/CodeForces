def solve():
    n = int(input())
    v = []
    r = 0
    mini = float('inf')

    for _ in range(n):
        m = int(input())
        v1 = list(map(int, input().split()))
        v1.sort()

        if m == -1:
            r += v1[0]
        else:
            k = v1[0]
            v.append(v1[1])
            mini = min(mini, k)

        r += mini

    v.sort()

# Calling the solve function
solve()
