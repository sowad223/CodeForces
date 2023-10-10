with open("input5_3.txt", "r") as file:
    num_cities, num_roads, D = map(int, file.readline().split())
    graph = [[] for _ in range(num_cities + 1)]
    for _ in range(num_roads):
        u, v = map(int, file.readline().split())
        graph[u].append(v)
        graph[v].append(u)

queue = [(1, [], 0)]
visited = [None] * (num_cities + 1)
visited[1] =1

while queue:
    node, path, current_time = queue.pop(0)
    if node == D:
        shortest_path = path + [node]
        time= current_time
        break
    for i in graph[node]:
        if not visited[i]:
            queue.append((i, path + [node], current_time + 1))
            visited[i] = True
with open("output5_3.txt", "w") as file:
        file.write("Shortest Path: " + " ".join(map(str, shortest_path)) + "\n")
        file.write(f"Time: {time}\n")


