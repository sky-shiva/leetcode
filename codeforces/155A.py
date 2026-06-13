n = int(input())
a = list(map(int,input().split()))
c=0
mx=a[0]
mn=a[0]
for i in range(1,n):
    if a[i]>mx:
        c+=1
        mx=a[i]
    elif a[i]<mn:
        c+=1
        mn=a[i]
print(c)