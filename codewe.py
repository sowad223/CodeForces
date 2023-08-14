t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    o=list(map(int,input().split()))
    j=0
    flag=False
    for i in o:
         if abs(d-i)%c==0 and abs(d-i)<=(b-1)*c and abs(d-i)>0:
             j+=1
             flag=True
    if not flag:
        print(0)
    else:
        print(j)