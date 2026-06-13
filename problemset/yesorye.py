t = int(input())

ans=[]
for _ in range(t):
    s = input()
    s=s.upper()
    if s=="YES":
        ans.append("YES")
    else:
        ans.append("NO")

for a in ans:
    print(a)
