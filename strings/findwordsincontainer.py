# You are given a 0-indexed array of strings words and a character x.

# Return an array of indices representing the words that contain the character x.

# Note that the returned array may be in any order.

x=input("Enter the string : ")

n=int(input("How many words you want to enter into the list of words : "))

words=[]

for i in range(n):
    word=input(f"Enter the {i} word : ")
    words.append(word)
    
    store_indices=[]
    
    for i in range(len(words)):
        if x in words[i]:
            store_indices.append(i)
    print(store_indices)