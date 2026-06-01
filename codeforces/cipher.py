n = int(input())
t = input()

ans = ""
i = 0
step = 1

while i < n:
    ans += t[i]
    i += step
    step += 1

print(ans)