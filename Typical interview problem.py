for i in range(int(input())):
    n=int(input())
    s=input()
    k=""
    flag=True
    for i in range(1,40):
        if i%3==0:
            k+='F'
        if i%5==0:
            k+="B"
    print(k)
    for i in range(8):
        if k[i:i+n]==s:
            flag=False
            break
    if flag==False:
        print("YES")
    else:
        print("NO")


