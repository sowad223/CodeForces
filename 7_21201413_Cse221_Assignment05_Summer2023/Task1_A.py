def dfs(course, g, v, s):
    v[course] = True
    for p in g[course]:
        if not v[p]:
            dfs(p, g, v, s)
    s.append(course)

def find_course_order(N, prerequisites):
    g = [[] for _ in range(N+1)]
    for a, b in prerequisites:
        g[b].append(a)
    v = [False] * (N+1)
    s = []

    for c in range(1, N+1):
        if not v[c]:
            dfs(c, g, v, s)

    return s[::-1]
with open("input1A_1.txt", "r") as file:
    N, M = map(int, file.readline().split())
    prerequisites = [list(map(int, file.readline().split())) for _ in range(M)]
course_order = find_course_order(N, prerequisites)
with open("output1A_1.txt", "w") as file:
    if len(course_order) == N:
        file.write(" ".join(map(str, course_order)))
    else:
        file.write("IMPOSSIBLE")


