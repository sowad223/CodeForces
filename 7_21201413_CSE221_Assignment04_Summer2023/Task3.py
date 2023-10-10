with open("input3_3.txt", "r") as file:
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

while stack:
    node = stack.pop()
    dfs_result.append(node)
    for i in graph[node]:
        if not visited[i]:
            stack.append(i)
            visited[i] = 1
        # else:
        #     print("YES")


with open("output3_3.txt", "w") as file:
    file.write(" ".join(map(str, dfs_result)))
