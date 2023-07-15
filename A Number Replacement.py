# for _ in range(int(input())):
#     n = int(input())
#     a =list(map(int,input().split()))
#     s = input()
#     m = {}
#     for i in range(n):
#         m[a[i]] = s[i]
#     for i in range(n):
#         if m[a[i]]!=s[i]:
#             print("NO")
#             break
#     else:
#         print("YES")
# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     s = input()
#     m = {}
#     ans = "YES"
#     for i in range(n):
#         if a[i] in m and m[a[i]] != s[i]:
#             ans = "NO"
#             break
#         else:
#             m[a[i]] = s[i]
#     print(ans)
with open("input1.txt", "r") as input_file, open("output1.txt", "w") as output_file:
    num_cases = int(input_file.readline().strip())

    for _ in range(num_cases):
        n = int(input_file.readline().strip())
        a = list(map(int, input_file.readline().strip().split()))
        s = input_file.readline().strip()

        m = {}
        ans = "YES"

        for i in range(n):
            if a[i] in m and m[a[i]] != s[i]:
                ans = "NO"
                break
            else:
                m[a[i]] = s[i]

        output_file.write(ans + "\n")
