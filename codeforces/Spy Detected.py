from collections import Counter

t = int(input())

ans=[]
for _ in range(t):
    n = int(input())
    
    l = list(map(int,input().split()))
   
    c  = Counter(l)
    
    for el ,f in c.items():
        if f>1:
            mostfreq=el
            break
    for i in range(n):
        if l[i]!=mostfreq:
            ans.append(i+1)
for x in ans:
    print(x)