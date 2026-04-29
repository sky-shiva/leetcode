#  Nick is working in a photo studio where his boss has given him a task to arrange the photos of family 
# members. He is French and he do not know English somehow, he managed to send the list of names to 
# you (his friend). Help Nick to sort the photos. 
# (Note: implement the odd even merge algorithm) 

n=int(input())

arr=[]

for i in range(n):
    name=input()
    arr.append(name)
    
sorted=False

while not sorted:
    sorted=True
    
    for i in range(1,n-1,2):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            sorted=False
            
    for i in range(0,n-1,2):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            sorted=False

print("Sorted the names using Odd - Even Merge : ")
for i in range(n):
    print(arr[i])