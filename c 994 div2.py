test_cases = int(input())

while test_cases > 0:
    test_cases -= 1

    n, x, y = map(int, input().split())

    assigned_values = [-1] * n
    friendships = [set() for _ in range(n)]

    # Defining friendships in a circle
    i = 0
    while i < n:
        friendships[i].add((i + 1) % n)
        friendships[i].add((i - 1 + n) % n)
        i += 1

    # Adding friendship between x and y
    x -= 1
    y -= 1
    friendships[x].add(y)
    friendships[y].add(x)

    # Assigning values ensuring the MEX condition
    i = 0
    while i < n:
        neighbor_values = set()
        for friend_index in friendships[i]:
            if assigned_values[friend_index] != -1:
                neighbor_values.add(assigned_values[friend_index])

        mex = 0
        while mex in neighbor_values:
            mex += 1

        assigned_values[i] = mex
        i += 1

    print(" ".join(map(str, assigned_values)))
