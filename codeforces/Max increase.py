n = int(input())

a = list(map(int,input().split()))

cc=1
s = 1

for i in range(0,n-1):
    
    if a[i]<a[i+1]:
        cc+=1
    else:
        s = max(s,cc)
        cc=1
print(max(s,cc))






