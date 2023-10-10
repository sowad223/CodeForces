for _ in range(int(input())):
    n=int(input())
    ele=list(map(int,input().split()))
    alice=[]
    bob=[]
    alice.append(ele[0])
    countB=0
    countA=0
    s=0
    for i in range(1,n):
        for m in bob:
            if  m< ele[i]:
                countB+=1
        for m in alice:
            if m<  ele[i]:
                countA+=1
        if countB==0 and countA!=0:
            bob.append(ele[i])
            s+=1
        alice.append(ele[i])
    print(s)

