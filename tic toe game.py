
def check_winner(a1, a2, a3):
    c = '.'
    for i in range(3):
        if a1[i] == a2[i] == a3[i] and a1[i] != '.':
            c = a1[i]

    if a1[0] == a1[1] == a1[2] and a1[0] != '.':
        c = a1[0]

    if a2[0] == a2[1] == a2[2] and a2[0] != '.':
        c = a2[0]

    if a3[0] == a3[1] == a3[2] and a3[0] != '.':
        c = a3[0]

    if a1[0] == a2[1] == a3[2] and a1[0] != '.':
        c = a1[0]

    if a3[0] == a2[1] == a1[2] and a3[0] != '.':
        c = a3[0]

    return c


t = int(input())

for _ in range(t):
    a1 = list(input())
    a2 = list(input())
    a3 = list(input())

    winner = check_winner(a1, a2, a3)

    if winner == '.':
        print("DRAW")
    else:
        print(winner)


