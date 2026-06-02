

n = int(input())

notes = [100, 20, 10, 5, 1]

count = 0

for note in notes:
    count += n // note
    n %= note

print(count)