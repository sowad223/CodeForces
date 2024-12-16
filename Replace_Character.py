for _ in range(int(input())):
    length = int(input())
    string = input()
    freq_dict = {}

    for char in string:
        if char not in freq_dict:
            freq_dict[char] = 1
        freq_dict[char] += 1

    sorted_freq = sorted(freq_dict.items(), key=lambda item: item[1])
    print(string.replace(sorted_freq[0][0], sorted_freq[-1][0], 1))
