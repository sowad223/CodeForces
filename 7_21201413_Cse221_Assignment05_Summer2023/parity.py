for _ in range(int(input())):
    n=int(input())
    k=list(map(int,input().split()))
    if (sum(k))%2==0:
        print("Yes")
    else:
        print("No")
