import math

n = int(input("Enter a number: "))

prime_factorials = []
adj = {}

i = 2
while i <= n:
    is_prime = True
    j = 2

    while j <= int(math.sqrt(i)):
        if i % j == 0:
            is_prime = False
            break
        j += 1
    if is_prime:
        adj[i] = []
        j = i * 2

        while j<=n:
            adj[i].append(j)
            j += i
    i += 1

i = 2
while i <= n:
    is_prime = True
    j = 2

    while j <= int(math.sqrt(i)):
        if i % j == 0:
            is_prime = False
            break

        j += 1
    if is_prime:
        prime_factorials.append(i)

        for j in adj[i]:
            is_prime_j = True
            k = 2

            while k <= int(math.sqrt(j)):
                if j % k == 0:
                    is_prime_j = False
                    break

                k += 1
            if is_prime_j:
                prime_factorials.append(j)
    i += 1

print(prime_factorials)
print(adj)


