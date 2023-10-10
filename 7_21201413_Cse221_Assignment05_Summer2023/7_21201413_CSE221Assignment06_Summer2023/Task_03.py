def minDistance(dist, sptSet):
    min_val = float('inf')
    min_index = -1
    for v in range(len(dist)):
        if dist[v] < min_val and not sptSet[v]:
            min_val = dist[v]
            min_index = v
    return min_index


def dijkstra(graph, src, n):
    dist = [float('inf')] * n
    dist[src] = 0
    sptSet = [False] * n

    for _ in range(n):
        u = minDistance(dist, sptSet)
        sptSet[u] = True

        for v in range(n):
            if (graph[u][v] > 0 and not sptSet[v] and
                    dist[v] > max(dist[u], graph[u][v])):
                dist[v] = max(dist[u], graph[u][v])

    return dist


def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        N, M = map(int, file.readline().split())
        graph = [[0] * N for _ in range(N)]

        for _ in range(M):
            u, v, w = map(int, file.readline().split())
            graph[u - 1][v - 1] = w  # Adjusting indices to 0-based

        return graph


def write_output_to_file(filename, danger_level):
    with open(filename, 'w') as file:
        if danger_level == float('inf'):
            file.write("Impossible\n")
        else:
            file.write(f"{danger_level}\n")
input_filename = "input3_1.txt"
output_filename = "output3_1.txt"

graph = read_graph_from_file(input_filename)
danger_levels = dijkstra(graph, 0, len(graph))  # Start from node 1 (0-based index)
write_output_to_file(output_filename, danger_levels[-1])
