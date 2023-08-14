for _ in range(int(input())):

    n = int(input())

    arr = list(map(int, input().split()))

    flag = True

    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            flag = False
            break

    if flag:
        print("0")
    else:
        k =n-1
        for i in range(n - 1, 0, -1):
            if arr[i] >= arr[i - 1]:
                continue
            else:
                k = i
                break
        print( max(arr[:k + 1]))

