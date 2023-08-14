def find_course_order(N, prerequisites):
    g = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    for a, b in prerequisites:
        g[a].append(b)
        indegree[b] += 1

    q = []
    for c in range(1, N + 1):
        if indegree[c] == 0:
            q.append(c)

    course_order = []
    while q:
        course = q.pop(0)
        course_order.append(course)
        for p in g[course]:
            indegree[p] -= 1
            if indegree[p] == 0:
                q.append(p)

    return course_order if len(course_order) == N else []
with open("input1B_1.txt", "r") as file:
    N, M = map(int, file.readline().split())
    prerequisites = [list(map(int, file.readline().split())) for _ in range(M)]
course_order = find_course_order(N, prerequisites)

with open("output1B_1.txt", "w") as file:
    if course_order:
        file.write(" ".join(map(str, course_order)))
    else:
        file.write("IMPOSSIBLE")
