import heapq

graph = {
    'A': [('E', 6)],
    'B': [('C', 3), ('D', -7), ('E', 5)],
    'C': [('D', 3)],
    'D': [('F', 11), ('G', 8)],
    'E': [('D', 4), ('G', -9)],
    'F': [('G', 5)],
    'G': []
}

distances = {vertex: float('inf') for vertex in graph}
distances['G'] = 0

priority_queue = [(0, 'G')]

while priority_queue:
    current_distance, current_vertex = heapq.heappop(priority_queue)

    if current_distance > distances[current_vertex]:
        continue

    for neighbor in graph:
        for adjacent, weight in graph[neighbor]:
            if adjacent == current_vertex:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

for vertex in distances:
    print(f"Shortest distance from {vertex} to G: {distances[vertex]}")
