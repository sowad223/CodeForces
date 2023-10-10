
with open("input1B_2.txt", "r") as file:
    n, m = map(int, file.readline().split())
    adj_list = {i: [] for i in range(n + 1)}
    for _ in range(m):
        u, v, w = map(int, file.readline().split())
        adj_list[u].append((v, w))

with open("output1B_2.txt", "w") as file:
    for vertex, edges in adj_list.items():
        file.write(f"{vertex} :")
        if edges:
            file.write(" ".join(f" ({adj_vertex},{weight})" for adj_vertex, weight in edges))
        file.write("\n")
