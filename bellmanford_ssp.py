edges = [
    ('A', 'E', 6),
    ('B', 'C', 3),
    ('B', 'D', -7),
    ('B', 'E', 5),
    ('C', 'D', 3),
    ('D', 'F', 11),
    ('D', 'G', 8),
    ('E', 'D', 4),
    ('E', 'G', -9),
    ('F', 'G', 5)
]

vertices = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
distances = {vertex: float('inf') for vertex in vertices}
distances['G'] = 0

for _ in range(len(vertices) - 1):
    for u, v, weight in edges:
        if distances[v] + weight < distances[u]:
            distances[u] = distances[v] + weight

for vertex, distance in distances.items():
    print(f"Shortest distance from {vertex} to G: {distance}")
