import sys

def solve():
    try:
        data = sys.stdin.read().split()
    except EOFError:
        return
    if not data:
        return
    
    p = 0
    t = int(data[p])
    p += 1
    
    out = []
    
    for _ in range(t):
        size = int(data[p])
        p += 1
        
        nums = [int(x) for x in data[p:p+size]]
        p += size
        
        res = [0] * size
        
        for idx in range(size):
            val_i = nums[idx]
            ev = []
            base = 0
            higher = 0
            
            for nxt in range(idx + 1, size):
                val_j = nums[nxt]
                
                if val_j > val_i:
                    higher += 1
                    ev.append(((val_i + val_j) // 2 + 1) * 2 + 1)
                
                elif val_j < val_i:
                    base += 1
                    ev.append(((val_i + val_j - 1) // 2 + 1) * 2)
            
            cur_score = base
            best = max(base, higher)
            
            if ev:
                ev.sort()
                for e in ev:
                    if e & 1:
                        cur_score += 1
                    else:
                        cur_score -= 1
                    
                    if cur_score > best:
                        best = cur_score
            
            res[idx] = best
        
        out.append(" ".join(map(str, res)))
    
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()