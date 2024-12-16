
matrix = []
for i in range(5):
    matrix.append(list(map(int, input().split())))


for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            r, c = i + 1, j + 1
            break


moves = abs(r - 3) + abs(c - 3)


print(moves)
