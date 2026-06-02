t = int(input())

listans = []
length = []

for _ in range(t):
    n = int(input())
    s = str(n)

    ans = ""
    l = len(s)

    for i in range(l):
        if s[i] != '0':
            ans += s[i] + ('0' * (l - i - 1)) + ' '

    listans.append(ans)
    length.append(len(ans.split()))
    print(type(ans))

for i in range(len(length)):
    print(length[i])
    print(listans[i])