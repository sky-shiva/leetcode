# You are given an integer array nums.

# The alternating sum of nums is the value obtained by adding elements at even indices and subtracting elements at odd indices. That is, nums[0] - nums[1] + nums[2] - nums[3]...

# Return an integer denoting the alternating sum of nums.

n=int(input("Enter the size of an array : "))
nums=[]
for i in range(n):
    num = int(input(f"Enter {n} numbers:  "))
    nums.append(num)

esum=0
osum=0
for i in range(len(nums)):
    if i%2==0:
        esum+=nums[i]
    else:
        osum+=nums[i]
     
print(esum-osum)

    