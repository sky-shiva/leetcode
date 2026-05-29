a,b,c,d=map(int,input().split())

l = []

l.append(a)
l.append(b)
l.append(c)
l.append(d)


dis=len(set(l))

print(4-dis)