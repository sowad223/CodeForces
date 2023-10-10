for _ in range(int(input())):
    n=input().strip()
    op=n.count("(")
    cl=n.count(")")
    flag=True
    if n=="()":
        print("NO")
        continue
    print("YES")
    # dict1={"(":len(n),")":len(n)}
    # res="(" * len(n)+ len(n) * ")"
    # if n in dict1:
    #     print("YES")
    #     print(res)
    # else:
    #     res=res[:1]+"(" + res[2:-1] + ")" + res[-1:]
    #     print("YES")
    #     print(res)
    res=["()"]*len(n)
    print(res)
    res1=["("] * len(n)
    print(res1)
    res2=[")"] * len(n)
    print(res2)
    result= res1+ res2
    if n in "".join(res):
        flag=False
        print("".join(result))
    else:
        print("".join(res))