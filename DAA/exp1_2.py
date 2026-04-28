def count_set_bits(n):
    return bin(n).count('1')

n=int(input())
arr=[]

for i in range(n):
    num=int(input())
    arr.append(num)
    arr.sort(key=count_set_bits,reverse=True)
print(arr)