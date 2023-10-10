def read_input_from_file(filename):
    with open(filename, 'r') as file:
        n, m = map(int, file.readline().split())
        arr = [[0] * (n + 1) for i in range(n + 1)]
        for _ in range(m):
            u, v, w = map(int, file.readline().split())
            arr[u][v] = w
    return arr

def write_output_to_file(arr, filename):
    with open(filename, 'w') as file:
        for row in arr:
            file.write(' '.join(map(str, row)) + '\n')

if __name__ == "__main__":
    input_filename = "input1A_1.txt"
    output_filename = "output1A_1.txt"

    arr = read_input_from_file(input_filename)
    write_output_to_file(arr, output_filename)
