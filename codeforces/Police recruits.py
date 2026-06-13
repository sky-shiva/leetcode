n=int(input())
l=list(map(int,input().split()))


of=0
un=0

for i in range(n):
    if l[i]!=-1:
        of+=l[i]
    if l[i]==-1:
        if of>0:
            of-=1
        else:
            un+=1
print(un)
