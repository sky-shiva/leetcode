t=int(input())

s = input()

l=[]
for i in range(t):
    l.append(s[i])
ns=""
for i in range(1,t+1):
    if i%2!=0:
        ns+=l[i]
print(ns)