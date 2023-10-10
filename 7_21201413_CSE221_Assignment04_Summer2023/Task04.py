with open("input4_4.txt", "r") as file:
    num_cities, num_roads = map(int, file.readline().split())
    graph = [[] for _ in range(num_cities + 1)]
    for _ in range(num_roads):
        u, v = map(int, file.readline().split())
        graph[u].append(v)
        graph[v].append(u)
visited = [None] * (num_cities + 1)
dfs_result = []
stack = [1]
visited[1] = 1
str=""
while stack:
    node = stack.pop()
    dfs_result.append(node)
    for i in graph[node]:
        if not visited[i]:
            stack.append(i)
            visited[i] = 1
with open("output4_4.txt", "w") as file:
    if dfs_result == list(range(1, num_cities + 1)):
        file.write("YES")
    else:
        file.write("NO")
