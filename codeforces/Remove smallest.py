t=int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(n-1):
        op=abs(a[i]-a[i+1])
        if op <=1:
            a.append(op)
    if len(set(a))==1:
        print("YES")
    else:
        print("NO")            