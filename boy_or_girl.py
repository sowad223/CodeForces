

username = input()

char_count = {}

for char in username:
    if char not in char_count:
        char_count[char] = 1

distinct_count = len(char_count)

if distinct_count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

