n = int(input())

l = list(map(int,input().split()))

gp=[]
ma=[]
pf=[]

for i in range(n):
    if l[i]==1:
        gp.append(i+1)
    elif l[i]==2:
        ma.append(i+1)
    else:
        pf.append(i+1)
        
gpl=len(gp)
mal=len(ma)
pfl=len(pf)

mnle=min(gpl,mal,pfl)

print(mnle)

for i in range(mnle):
    print(gp[i],ma[i],pf[i])
