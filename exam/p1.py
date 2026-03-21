import sys

data = sys.stdin.read().split()
idx = 0

t = int(data[idx])
idx += 1

out = []

for _ in range(t):
    n = int(data[idx])
    c = int(data[idx + 1])
    k = int(data[idx + 2])
    idx += 3

    arr = list(map(int, data[idx:idx + n]))
    idx += n

    arr.sort()
    power = c
    flips = k

    for val in arr:
        if val > power:
            break
        add = min(flips, power - val)
        power += val + add
        flips -= add

    out.append(str(power))

print("\n".join(out))