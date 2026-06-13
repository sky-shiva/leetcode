t = int(input())
ans=[]
for _ in range(t):
    a,b,c=map(int,input().split())
    if a+b==c or b+c==a or c+a==b:
        ans.append("YES")
    else:
        ans.append("NO")
for a in ans:
    print(a,sep='\n')