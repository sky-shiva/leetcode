# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.

n=int(input("Enter the size of the array : "))
extracandies=int(input("Enter the extra candies u have : "))

candies=[]
b_e=[]

for i in range(n):
    c=int(input("Enter candy: "))
    candies.append(c)

max_c=max(candies)

for candy in candies:
    if candy + extracandies >=max_c:
        b_e.append(True)
    else:
        b_e.append(False)
print(b_e)