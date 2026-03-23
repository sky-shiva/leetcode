# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

s=input()
j=input()

count=0
for i in range(len(j)):
    if j[i] in s:
        count+=1
print(count)

