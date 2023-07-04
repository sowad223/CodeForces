t=int(input())
for i in range(t):
    s = "codeforces"
    n = len(s)
    k=input()
    count=0
    for j in range(n):
            if k[j]!=s[j]:
                count+=1
    print(count)