t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    print(2 * max(arr) - sum(arr))