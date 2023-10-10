def solve():
    n = input()
    pos = len(n)
    for i in range(len(n) - 1, -1, -1):
        if int(n[i]) >= 5:
            if i == 0:
                n = '1' + n
                pos = i + 1
            else:
                n = n[:i-1] + str(int(n[i-1]) + 1) + n[i:]
                pos = i
    n = n[:pos] + '0' * (len(n) - pos)
    print(n)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()


