t=int(input())

for _ in range(t):
    a,b=map(int,input().split())
    
    rem = a%b
    if rem==0:
        print(0)
    else:
        print(b-rem)