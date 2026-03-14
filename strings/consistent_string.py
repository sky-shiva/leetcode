# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent 
# if all characters in the string appear in the string allowed.
# Return the number of consistent strings in the array words.

allowed=input("Enter the allowed Characters : ")
n=int(input("Enter the number of words : "))
words=[]

for i in range(n):
    word=input()
    words.append(word)
    
allowed_set=set(allowed)
count=0

for i in range(len(words)):
    convert=set(words[i])
    
    if convert.issubset(allowed_set):
        count+=1
print(count)