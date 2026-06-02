n = int(input())
feeling = []
for i in range(1, n + 1):
    if i % 2 == 1:
        feeling.append("I hate")
    else:
        feeling.append("I love")
print(" that ".join(feeling) + " it")
print(feeling)