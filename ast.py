for _ in range(int(input())):
    n=int(input())
    m=list(map(int,input().split()))
    count=0
    for i in range(n):
        if m[i]==(i+1):
            count+=1
        else:
            count+=0
    print((count+1)//2)


