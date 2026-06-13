from collections import Counter
s1=input()
s2=input()
comb=input()

lens1=len(s1)
lens2=len(s2)


if lens1+lens2 != len(comb):
    print("NO")
else:
    freq1=Counter(s1)
    freq2=Counter(s2)
    freqcomb=Counter(comb)
    try:
        add=freq1+freq2
    except Exception:
        print("NO")
    else:
        if add==freqcomb:
            print("YES")
        else:
            print("NO")
