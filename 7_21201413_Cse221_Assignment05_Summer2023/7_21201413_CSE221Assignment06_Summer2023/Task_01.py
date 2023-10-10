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


def readGraphFromFile(filename):
    with open(filename, 'r') as file:
        n, m = map(int, file.readline().split())
        graph = [[0] * n for _ in range(n)]

        for _ in range(m):
            u, v, w = map(int, file.readline().split())
            graph[u - 1][v - 1] = w
        source = int(file.readline().strip())
        return graph, source - 1, n


def writeSolutionToFile(filename, dist):
    with open(filename, 'w') as file:
        for distance in dist:
            if distance == float('inf'):
                file.write("-1 ")
            else:
                file.write(str(distance) + " ")
input_filename = "input1_1.txt"
output_filename = "output1_1.txt"

graph, source_vertex, num_vertices = readGraphFromFile(input_filename)
distances = dijkstra(graph, source_vertex, num_vertices)
writeSolutionToFile(output_filename, distances)
