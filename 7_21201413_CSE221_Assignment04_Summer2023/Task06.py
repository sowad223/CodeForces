with open("input6_2.txt", "r") as f:
    R, C = map(int, f.readline().split())

    g = []
    for _ in range(R):
        row = f.readline().strip()
        g.append(row)

visited = []
for _ in range(R):
    row=[None for _ in range(C)]
    visited.append(row)
max_diamonds = 0

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for r in range(R):
    for c in range(C):
        if g[r][c] == 'D' and not visited[r][c]:
            stack = [(r, c)]
            visited[r][c] = True
            diamonds = 0

            while stack:
                x, y = stack.pop()
                diamonds += 1 if g[x][y] == 'D' else 0

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and g[nx][ny] != '#':
                        stack.append((nx, ny))
                        visited[nx][ny] = True

            max_diamonds = max(max_diamonds, diamonds)

with open("output6_2.txt", "w") as f:
    f.write(str(max_diamonds) + "\n")
