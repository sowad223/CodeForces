
def f(x, y, d):
    t = ((y - x) % d) == 0
    return (y - x) // d + 1 - t

def main():
    t = int(input())
    for _ in range(t):
        n, m, d = map(int, input().split())
        v = list(map(int, input().split()))
        s = 0
        if v[0] != 1:
            s = 1
            v.insert(0, 1)
        v.append(n + 1)
        n = len(v)
        a = 0
        for i in range(1, n):
            a += f(v[i - 1], v[i], d)
        a2 = a
        n_a = a
        for i in range(1, n - 1):
            c = f(v[i - 1], v[i + 1], d) - f(v[i - 1], v[i], d) - f(v[i], v[i + 1], d)
            n_a = a2 + c
            a = min(a, n_a)
        c = 0
        for i in range(1, n - 1):
            cur = f(v[i - 1], v[i + 1], d) - f(v[i - 1], v[i], d) - f(v[i], v[i + 1], d)
            n_a = a2 + cur
            if n_a == a:
                c += 1
        if a == a2 and s == 0:
            c += 1
        print(a, c)

if __name__ == "__main__":
    main()
