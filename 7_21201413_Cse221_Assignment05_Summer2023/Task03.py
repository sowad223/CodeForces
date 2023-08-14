def dfs(node, graph, visited, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, stack)
    stack.append(node)


def transpose(graph):
    transposed = [[] for _ in range(len(graph))]
    for node in range(len(graph)):
        for neighbor in graph[node]:
            transposed[neighbor].append(node)
    return transposed


def find_scc(N, edges):
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u - 1].append(v - 1)

    visited = [False] * N
    stack = []

    for node in range(N):
        if not visited[node]:
            dfs(node, graph, visited, stack)

    transposed = transpose(graph)
    visited = [False] * N
    components = []

    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            dfs(node, transposed, visited, component)
            components.append(component)

    return components


with open("input3_1.txt", "r") as file:
    N, M = map(int, file.readline().split())
    edges = []
    for _ in range(M):
        u, v = map(int, file.readline().split())
        edges.append((u, v))


scc = find_scc(N, edges)


with open("output3_1.txt", "w") as file:
    for component in scc:
        file.write(" ".join(str(node + 1) for node in component) + "\n")

