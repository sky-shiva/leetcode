# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

# For each index i, names[i] and heights[i] denote the name and height of the ith person.

# Return names sorted in descending order by the people's heights.

# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: M


n=int(input("Enter the size of names,heights both are considered as same: " ))

names=[]

heights=[]

for i in range(n):
    name=input(f"Enter the {i} name : ")
    height=int(input(f"Enter the {i} height : "))
    names.append(name)
    heights.append(height)

# print("before: ")

# print(names)
for i in range(n):
    for j in range(i+1,n):
        if heights[i]>heights[j]:
            temp,tempn=heights[i],names[i]
            heights[i],names[i]=heights[j],names[j]
            heights[j],names[j]=temp,tempn
print(heights)
print(names)
# print(heights)