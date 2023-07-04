for _ in range(int(input())):
    n = int(input())
    arr =list(map(int, input().split()))
    maxv=-1
    minv=float("inf")
    for i in arr:
        maxv=max(i,maxv)
        minv=min(i,minv)
    if minv<0:
        print(minv)
    else:
        print(maxv)
