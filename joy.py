
for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ans1=[]
    ans2=[]
    for i in range(n):
        if arr[i]%k==0:
            ans1.append(i+1)
        else:
            ans2.append((arr[i]%k,i+1))
    ans2.sort(key=lambda x:(x[0]),reverse=True)


    for i in ans2:
        ans1.append(i[1])
    for i in ans1:
        print(i,end=" ")
    print()

