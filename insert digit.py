for _ in range(int(input())):
    n, k = input().split()
    num = input()
    for i in range(len(num)):
        if num[i] < k:
            result = num[:i] + k + num[i:]
            break
    else:
        result = num + k
    print(result)

