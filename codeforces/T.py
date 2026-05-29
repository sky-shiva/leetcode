a,b,c,d=map(int,input().split())

list=[]

list.append(a)
list.append(b)
list.append(c)
list.append(d)

list.sort()
ans_l=[]

ansa = abs(list[0]-list[-1])
ans_b = abs(list[1]-list[-1])
ans_c = abs(list[2]-list[-1])

ans_l.append(ansa)
ans_l.append(ans_b)
ans_l.append(ans_c)

res = " ".join(str(x) for x in ans_l)

print(res)
