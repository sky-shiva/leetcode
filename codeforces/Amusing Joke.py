from collections import Counter

s1 = input()
s2 = input()
comb = input()

if len(s1) + len(s2) != len(comb):
    print("NO")
elif Counter(s1) + Counter(s2) == Counter(comb):
    print("YES")
else:
    print("NO")