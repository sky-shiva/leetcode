# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".


address=input("Enter the ip address : ")

modified=[]

for ch in address:
    if ch=='.':
        modified.append("[.]")
    else:
        modified.append(ch)
print(modified)