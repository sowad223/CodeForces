class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if root_x != root_y:
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

    def KruskalMST(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = sum(weight for u, v, weight in result)
        return minimumCost

def main():
    input_filename = "input1_1.txt"
    output_filename = "output1_1.txt"

    with open(input_filename, "r") as input_file:
        V, E = map(int, input_file.readline().split())
        g = Graph(V)
        for _ in range(E):
            u, v, w = map(int, input_file.readline().split())
            g.addEdge(u - 1, v - 1, w)

    with open(output_filename, "w") as output_file:
        result = g.KruskalMST()
        output_file.write(str(result))

if __name__ == '__main__':
    main()

