# 1) Angelina is an intelligent girl, every time she wins in any contest or programme, and solves complex 
# problems so I want to give her a challenge problem that is. Sort an array of strings according to string 
# lengths. If you are smarter than her, try to solve the problem faster than her? 
# Input 
# You 
# Output 
# You 
# are 
# are 
# beautiful 
# looking 
# looking 
# beautiful

n=int(input())

arr=[]

for i in range(n):
    str=input().split()
    arr.append(str)
arr.sort(key=len)
print(arr)
        
