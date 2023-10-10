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
                    dist[v] > dist[u] + graph[u][v]):
                dist[v] = dist[u] + graph[u][v]

    return dist


def find_meeting_point(graph, start_a, start_b):
    distances_a = dijkstra(graph, start_a, len(graph))
    distances_b = dijkstra(graph, start_b, len(graph))

    min_time = float('inf')
    meeting_node = -1

    for node in range(len(graph)):
        if distances_a[node] < float('inf') and distances_b[node] < float('inf'):
            total_time = max(distances_a[node], distances_b[node])
            if total_time < min_time:
                min_time = total_time
                meeting_node = node

    return min_time, meeting_node


def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        N, M = map(int, file.readline().split())
        graph = [[0] * N for _ in range(N)]

        for _ in range(M):
            u, v, w = map(int, file.readline().split())
            graph[u - 1][v - 1] = w  # Adjusting indices to 0-based

        S, T = map(int, file.readline().split())
        return graph, S - 1, T - 1


def write_output_to_file(filename, time, node):
    with open(filename, 'w') as file:
        if time == float('inf'):
            file.write("Impossible\n")
        else:
            file.write(f"Time {time}\nNode {node + 1}\n")
input_filename = "input2_1.txt"
output_filename = "output2_1.txt"

graph, start_a, start_b = read_graph_from_file(input_filename)
time, meeting_node = find_meeting_point(graph, start_a, start_b)
write_output_to_file(output_filename, time, meeting_node)
