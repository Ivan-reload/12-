n = bin(400)[2:]
ep = len(n)

def f(pos, l, q):
    if pos == ep:
        return ''.join(l)
    
    n = l[pos]
    if q == 1:
        if n == '0': l[pos], q = '1', 1
        elif n == '1': l[pos], q = '0', 1
    
    return f(pos+1, l, q)


print(int(f(0, list(n), 1), 2))
