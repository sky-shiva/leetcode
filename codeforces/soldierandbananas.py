k,n,w = map(int,input().split())

tc=0

for i in range(1, w + 1):
    tc += i*k

borrow=tc-n

if borrow<0:
    print(0)
else:
    print(borrow)