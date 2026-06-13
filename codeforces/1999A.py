t = int(input())
l=[]
for _ in range(t):
    s=0
    n =int(input())
    while n!=0:
        d = n%10
        s = s+d
        n=n//10
    l.append(s)
for ans in l:
    print(ans,sep="\n")