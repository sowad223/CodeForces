k = int(input())

for i in range(k):
    s = input()
    n = len(s)
    count = 0
    if n % 2 == 0 and n > 2:
        for m in range(1, n // 2):
            if s[m] != s[m - 1]:
                count += 1
                break
    elif n % 2 != 0 and n > 3:
        for j in range(1, n // 2):
            if s[j] != s[j - 1]:
                count += 1
                break
    if count > 0:
        print("YES")
    else:
        print("NO")