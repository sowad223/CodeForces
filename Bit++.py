n=int(input())
count=0
for i in range(n):
    s=input()
    if "++" in s:
        count+=1
    if "--" in s:
        count-=1
print(count)
