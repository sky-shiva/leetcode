s1,s2,s3,s4=map(int,input().split()) # calories

s = input()

l=[]

l.append(s1)
l.append(s2)
l.append(s3)
l.append(s4)


ad=0
for strip in s:
    if strip=='1':
        ad=ad+l[0]
    elif strip=='2':
        ad=ad+l[1]
    elif strip=='3':
        ad=ad+l[2]
    elif strip=='4':
        ad=ad+l[3]
print(ad)

