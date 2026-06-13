t = int(input())

l=[]
for _ in range(t):
    a,b,c=map(int,input().split())
    if a+b==c:
        l.append('+')
    else:
        l.append('-')
for ans in l:
    print(ans,sep="\n")