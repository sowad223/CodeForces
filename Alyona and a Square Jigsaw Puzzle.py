for _ in range(int(input())):
    n = int(input())
    pieces = list(map(int, input().split()))

    total_pieces = 0
    current_layer = 0
    happy_days = 0

    
    for day_pieces in pieces:
        total_pieces += day_pieces


        while total_pieces >= 1 + 8 * (current_layer * (current_layer + 1)) // 2:
            current_layer += 1


        if total_pieces == 1 + 8 * (current_layer * (current_layer - 1)) // 2:
            happy_days += 1

    print(happy_days)
