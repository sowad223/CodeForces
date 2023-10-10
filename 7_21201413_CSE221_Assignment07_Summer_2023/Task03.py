
with open("input3_1.txt", "r") as input_file:
    num_people, num_queries = map(int, input_file.readline().split())
    queries = []
    for _ in range(num_queries):
        person_a, person_b = map(int, input_file.readline().split())
        queries.append((person_a, person_b))
friend_circles = {i: {i} for i in range(1, num_people + 1)}
def find_friend_circle(person):
    for circle, members in friend_circles.items():
        if person in members:
            return circle
output_sizes = []
for person_a, person_b in queries:
    circle_a = find_friend_circle(person_a)
    circle_b = find_friend_circle(person_b)
    if circle_a != circle_b:
        friend_circles[circle_a] |= friend_circles[circle_b]
        del friend_circles[circle_b]
    output_sizes.append(len(friend_circles[circle_a]))
with open("output3_1.txt", "w") as output_file:
    for size in output_sizes:
        output_file.write(str(size) + "\n")
