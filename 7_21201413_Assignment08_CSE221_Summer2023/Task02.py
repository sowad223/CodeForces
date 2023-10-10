
with open("input2_4.txt", "r") as input_file:
    N = int(input_file.readline().strip())
if N <= 1:
    distinct_ways = 1
else:
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    distinct_ways = dp[N]

with open("output2_4.txt", "w") as output_file:
    output_file.write(str(distinct_ways))
