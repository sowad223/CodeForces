for i in range(int(input())):
    n=int(input())
    s=input()
    res=[]
    for i in range(n-1):
        m=s[i:i+2]
        if m not in res:
            res.append(m)
    print(len(res))
