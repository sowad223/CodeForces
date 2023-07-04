for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    res = 0
    flag = False
    s = 0
    for i in arr:
        if not i:
            continue
        s += abs(i)
        if i < 0:
            flag = True
        else:
            if flag:
                res += 1
                flag = False
    if flag:
        res += 1
    print(s, res)