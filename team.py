
n = int(input())
def count_problems(n, total):
  if n == 0:
    return total
  else:
    problem = list(map(int, input().split()))
    sure = sum(problem)
    if sure >= 2:
      return count_problems(n-1, total+1)

    else:
      return count_problems(n-1, total)


print(count_problems(n, 0))
