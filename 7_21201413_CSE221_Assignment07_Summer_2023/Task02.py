
with open("input2_1.txt", "r") as input_file:
    n, m = map(int, input_file.readline().split())
    tasks = []
    for i in range(n):
        a, b = map(int, input_file.readline().split())
        tasks.append((a, b))

def ta(task):
    return task[1]

sorted_task = sorted(tasks, key=ta)
complete = 0
people = [0] * m

for task in sorted_task:
    for i in range(m):
        if people[i] <= task[0]:
            people[i] = task[1]
            complete += 1
            break
with open("output2_1.txt", "w") as output_file:
    output_file.write(str(complete) + "\n")
