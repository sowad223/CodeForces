for  _ in range(int(input())):
    n=int(input())
    for i in range(n):
        a=list(map(int,input().split()))
        if len(a)==1:
            print("NO")
        count=0
        sum=0
        for i in a:
            count+=i==1
            sum+=i
    if sum>count:
        print("YES")
    else:
        print("NO")


