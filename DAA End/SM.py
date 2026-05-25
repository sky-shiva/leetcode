a11=int(input())
a12=int(input())
a21=int(input())
a22=int(input())

b11=int(input())
b12=int(input())
b21=int(input())
b22=int(input())

p = (a11 + a22) * (b11 + b22)
q = (a21 + a22) * b11
r = a11 * (b12 - b22)
s = a22 * (b21 - b11)
t = (a11 + a12) * b22
u = (a21 - a11) * (b11 + b12)
v = (a12 - a22) * (b21 + b22)

c11 = p + s - t + v
c12 = r + t
c21 = q + s
c22 = p - q + r + u

print(c11, c12)
print(c21, c22)