
with open("input1_1.txt", "r") as input_file:
    n = int(input_file.readline().strip())
    task = []
    for i in range(n):
        a, b = map(int, input_file.readline().strip().split())
        task.append((a, b))

def tasks(task12):
    return task12[1]

sorted_task = sorted(task, key=tasks)
time = 0
complete = []

for task12 in sorted_task:
    if task12[0] >= time:
        complete.append(task12)
        time = task12[1]

with open("output1_1.txt", "w") as output_file:
    output_file.write(str(len(complete)) + "\n")
    for task12 in complete:
        output_file.write(str(task12[0]) + " " + str(task12[1]) + "\n")
