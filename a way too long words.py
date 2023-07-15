i = int(input())

for _ in range(0,i):
    s = str(input())
    l = len(s)
    count=0
    if len(s)>10:
        count+=1
        print(s[0]+str(len(s)-2)+s[-1])
    else:
        print(s)

4

