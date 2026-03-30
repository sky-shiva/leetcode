# # vowel string test case 1 : aeioueo->yes case 2: ovbwe -> no

st=input()

vowels='aeiou'
if st in vowels:
    print("Yes")
else:
    print("No")

# is this correct code fo  r the above problem statement?The code you provided checks if the entire input string `st` is a single vowel (one of 'a', 'e', 'i', 'o', 'u'). However, the problem statement seems to be asking whether the string contains only vowels, not just if it is a single vowel.
# To check if the string contains only vowels, you can modify the code as follows:
# st = inpu() # aeioueue
# vowels = 'aeiou'
# is_vowel_string = all(char in vowels for char in st)
# if is_vowel_string:
#     print("Yes")
# else: 
#     print("No")    

# st=input()

# vowels='aeiou'
# is_vowel=True

# for char in st:
#     if char not in vowels:
#         is_vowel=False
#         break
#     else:
#         continue
# if is_vowel:
#     print("Yes")
# else:    print("No")