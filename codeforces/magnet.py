n = int(input())

a = [input() for _ in range(n)]

g = 1
for i in range(1,n):
    if a[i]!=a[i-1]:
        g+=1
print(g)