n = int(input())

s = input().lower()

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for ch in s:
    if ch in letters:
        letters.remove(ch)

if len(letters)==0:
    print("YES")
else:
    print("NO") # submitted in codeforces