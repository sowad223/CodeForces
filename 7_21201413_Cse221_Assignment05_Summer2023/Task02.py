def dfs(node, graph, visited, result):
    visited[node] = 1

    for neighbor in graph[node]:
        if visited[neighbor] == 1:
            return ["IMPOSSIBLE"]
        elif visited[neighbor] == 0:
            result = dfs(neighbor, graph, visited, result)

    visited[node] = 2
    result.append(node)
    return result


def find_lexicographically_smallest_sequence(num_courses, prerequisites):
    course_graph = [[] for _ in range(num_courses + 1)]
    for course, prereq in prerequisites:
        course_graph[course].append(prereq)

    visited_status = [0] * (num_courses + 1)
    result_sequence = []

    for i in range(1, num_courses + 1):
        if visited_status[i] == 0:
            result_sequence = dfs(i, course_graph, visited_status, result_sequence)
            if result_sequence[0] == "IMPOSSIBLE":
                return result_sequence

    return result_sequence[::-1]

with open("input2_2.txt", "r") as file:
    num_courses, num_prerequisites = map(int, file.readline().split())
    prerequisites_list = []
    for _ in range(num_prerequisites):
        course_A, course_B = map(int, file.readline().split())
        prerequisites_list.append((course_A, course_B))


lexicographically_smallest_seq = find_lexicographically_smallest_sequence(num_courses, prerequisites_list)

with open("output2_2.txt", "w") as file:
    if lexicographically_smallest_seq[0] == "IMPOSSIBLE":
        file.write(lexicographically_smallest_seq[0])
    else:
        file.write(" ".join(map(str, lexicographically_smallest_seq)))
