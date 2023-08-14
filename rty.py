def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort()

        i = 0
        ans = 0
        for i in range(n):
            j = i + 1
            while j<n:
                if a[j] - a[j - 1] > k:
                    break
                j += 1
            tt = j - i
            ans = max(ans, tt)
            i = j

        print(n - ans)

if __name__ == "__main__":
    main()