# In-Lab: 
# 1) Write a program for Naïve method to check whether a pattern is present in a string or not. Using 
# clock function find execution time and calculate the time complexity of the program. 
# Sample program with function which calculate execution time: 

import time

str=input()
pattern=input()

start_time=time.perf_counter()
l = len(str)-len(pattern)+1
for i in range(l):
    if str[i:i+len(pattern)]==pattern:
        print("Pattern Found")
        break
else:
    print("Pattern not found")
    
end_time=time.perf_counter()

print("Execution time: ",end_time-start_time)