
import math

for i in range(int(input())):
    n, k = map(int, input().split())
    min_ones = math.ceil((n - 1) / k) + 1
    print(min_ones)