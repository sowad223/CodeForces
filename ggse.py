for _ in range(int(input())):
    scores = list(map(int, input().split()))
    k=sorted(scores)
    if k[1]+k[2]>=10:
        print("Yes")
    else:
        print("NO")


