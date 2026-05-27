s = input()
distinct_letters = set()
for ch in s:
    if ch.isalpha():
        distinct_letters.add(ch)
print(len(distinct_letters))