# n=int(input())

# l=[]

# for i in range(1,n+1):
#     l.append(i)

# es=0
# os=0

# for i in range(n):
#     if i%2==0:
#         es+=-l[i]
#     else:
#         os+=l[i]
        
# print(es+os)

n=int(input())

index=0
es=0
os=0
for i in range(1,n+1):
    if index%2==0:
        es+=-i
    else:
        os+=i
    index+=1
print(es+os)

