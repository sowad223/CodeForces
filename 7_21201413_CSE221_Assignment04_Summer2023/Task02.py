
with open("input2_1.txt", "r") as file:
    num_cities, num_roads = map(int, file.readline().split())
    graph = [[] for _ in range(num_cities + 1)]
    for _ in range(num_roads):
        u, v = map(int, file.readline().split())
        graph[u].append(v)
        graph[v].append(u)
queue = [1]
visited = [0] * (num_cities + 1)
visited[1] = 1
bfs_result = []

while queue:
    node = queue.pop(0)
    bfs_result.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            queue.append(neighbor)
            visited[neighbor] = 1
with open("output2_1.txt", "w") as file:
    file.write(" ".join(map(str, bfs_result)))
