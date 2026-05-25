red,blue = map(int,input().split())

fashion = min(red,blue)

normal = (max(red,blue)-fashion)//2

print(fashion,normal)