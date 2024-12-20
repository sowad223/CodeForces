def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        v = list(map(int, input().split()))

        found = 0
        nonzero = 0

        for i in v:
            if i != 0 and not nonzero:
                found += 1
                nonzero = 1
            if i == 0:
                nonzero = 0

        print(min(2, found))


if __name__ == "__main__":
    solve()
