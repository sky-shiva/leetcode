t = int(input())

for _ in range(t):
    se={}
    n,m = map(int,input().split())
    for i in range(n):
        s = input()
        key = ''.join(sorted(s))
        print(key)
        for strings in s:
            sorr=sorted(strings)
            if key==sorr:
                if strings in key:
                    se[key]=strings
                else:
                    pass
    print(len(se))

        
        