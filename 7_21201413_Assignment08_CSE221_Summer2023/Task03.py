
with open("input3_1.txt", "r") as input_file:
    N, X = map(int, input_file.readline().split())
    coins = list(map(int, input_file.readline().split()))

INF = float('inf')
dp = [0] + [INF] * X

for i in range(1, X + 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)

result = dp[X] if dp[X] != INF else -1
with open("output3_1.txt", "w") as output_file:
    output_file.write(str(result))
