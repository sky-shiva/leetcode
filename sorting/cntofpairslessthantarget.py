# Given a 0-indexed integer array nums of length n and an integer target
# return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
# nums = [-1,1,2,3,1], target = 2
# Output: 3

target=int(input("Enter the target : "))
n=int(input("Enter the size of list : "))

nums=[]
count=0

# inserting the elements into the nums list.......
for i in range(n):
    num=int(input())
    nums.append(num)

for i in range(n):
    for j in range(i+1,n):
        if nums[i]+nums[j]<target:
            count+=1
print(f"Count is {count}")