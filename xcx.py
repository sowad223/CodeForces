for i in range(int(input())):
    n=int(input())
    count=0
    a1=[]
    b1=[]
    for i in range(n):
        a,b=map(int,input().split())
        a1.append(a)
        b1.append(b)
        if a1[i]>b1[i]:
            count+=1
    print(count)
