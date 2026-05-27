n = int(input())

arr = list(map(int,input().split()))


for i in range(1,n+1):
    s = i
    if s in arr:
        print(arr.index(s)+1,end=" ")
