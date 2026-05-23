s=input().strip

if s=="":
    print(0)
else:   
    remove_comma=s.split(",")
    dis=set(remove_comma)
    print(len(dis))