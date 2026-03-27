
# 1. Find first factor a
#    loop i from 2 to sqrt(n):
#        if n % i == 0:
#            a = i
#            break

# 2. n = n / a

# 3. Find second factor b
#    loop j from a+1 to sqrt(n):
#        if n % j == 0:
#            b = j
#            break

# 4. c = remaining = n / b

# 5. Check:
#    c != a and c != b and c > 1

# 6. If valid → YES
#    else → NO

import math
t=int(input())

for _ in range(t):
    n=int(input())
    a=b=0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            a=i
            break
    if a==0:
        print("NO")
        continue
    n=n//a
    for j in range(a+1,int(math.sqrt(n))+1):
        if n%j==0:
            b=j
            break
    if b==0:
        print("NO")
        continue
    c=n//b
    
    if c!=a and c!=b and c>1:
        print("YES")
        print(a,b,c)
    else:
        print("NO")