for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]


    def longest_blank_space(arr):
        if len(arr) == 1 and arr[0] == 0:
            return 1
        count = 0
        max_count = 0
        for i in arr:
            if i == 0:
                count += 1

            else:
                if count > max_count:
                    max_count = count
                count = 0
        if count > max_count:
            max_count = count
        return max_count


    print(longest_blank_space(arr))