import heapq


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    predecessors = {vertex: None for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors


# Read input from file
with open("input12.txt", "r") as file:
    num_vertices = int(file.readline().strip())
    num_edges = int(file.readline().strip())

    graph = {}
    for i in range(1, num_vertices + 1):
        graph[str(i)] = {}

    for _ in range(num_edges):
        source, target, weight = file.readline().strip().split()
        graph[source][target] = int(weight)

    start_vertex = file.readline().strip()

# Perform Dijkstra's algorithm
distances, predecessors = dijkstra(graph, start_vertex)

# Write output to file
with open("output12.txt", "w") as file:
    file.write("Shortest distances from " + start_vertex + "\n")
    for vertex, distance in distances.items():
        file.write(f"To {vertex}: {distance}\n")

print("Output written to output.txt")


