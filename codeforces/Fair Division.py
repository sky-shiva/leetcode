t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    total = sum(a)

    if total % 2 != 0:
        print("NO")

    elif a.count(1) == 0 and (total // 2) % 2 != 0:
        print("NO")

    else:
        print("YES")