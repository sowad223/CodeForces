s = input()
summands = [int(x) for x in s.split('+')]
summands.sort()
new_sum = '+'.join(str(x) for x in summands)
print(new_sum)
