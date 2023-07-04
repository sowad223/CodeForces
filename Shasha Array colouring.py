t=int(input())
for i in range(t):
    n=int(input())
    arr = list(map(int, input().split()))
    maxcost=0
    while len(arr)>1:
        k=max(arr)
        m=min(arr)
        maxcost+=max(arr)-min(arr)
        arr.remove(k)
        arr.remove(m)
    print(maxcost)