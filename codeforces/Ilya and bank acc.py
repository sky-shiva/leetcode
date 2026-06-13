n = int(input())


if n>0:
    print(n)
else:
    s = str(n)
    a = s[:-1]
    b = s[:-2]+s[-1]
    print(max(int(a),int(b)))