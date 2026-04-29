n=int(input())

jobs=[]

for i in range(n):
    name=input("Enter the job name : ");
    deadline=int(input("Enter the deadline : "))
    profit=int(input("Enter the profit : "));
    jobs.append((name,deadline,profit))
    
jobs.sort(key=lambda x:x[2],reverse=True)

max_deadline=max(j[1] for j in jobs)

slots=[-1]*max_deadline+1

profit=0
for job in jobs:
    for t in range(job[1],0,-1):
        if slots[t]==-1:
            slots[t]=job[0]
            profit+=job[2]
            break

print("Maximum profit:", profit)