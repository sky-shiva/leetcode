s = input()

distinct_letters = set()

for char in s:
    if 'a' <= char <= 'z':
        distinct_letters.add(char)

print(len(distinct_letters))
