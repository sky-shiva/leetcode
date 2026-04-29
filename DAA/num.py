import numpy as np
a11=int(input())
a12=int(input())
a21=int(input())
a22=int(input())

b11=int(input())
b12=int(input())
b21=int(input())
b22=int(input())

A=np.array([[a11,a12],[a21,a22]])
B=np.array([[b11,b12],[b21,b22]])

st = np.matmul(A,B)

print(st)