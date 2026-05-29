n = int(input())
capacity = 0
current_passengers = 0
for _ in range(n):
    a, b = map(int, input().split())
    current_passengers -= a
    current_passengers += b
    capacity = max(capacity, current_passengers)
print(capacity)