for _ in range(int(input())):
    b,c,h=list(map(int,input().split()))
    flag=False
    while b>=c+h:
        if b-1>=c+h:
            print(2*(c+h)+1)
        else:
            print(2*b-1)
        flag=True
        break
    if not flag:
        print(2*b-1)
