n = bin(204)[2:]
sp = len(n)-1

def f(pos, l, q):
    if pos < 0:
        return ''.join(l)
    
    n = l[pos]
    if q == 1:
        if n == '0': l[pos], q = '1', 2
        elif n  == '1': l[pos], q = '0', 2
    
    elif q == 2:
        if n == '0': l[pos], q = '1', 3
        elif n == '1': l[pos], q = '0', 2
    
    elif q == 3:
        if n == '0': l[pos], q = '0', 2
        elif n == '1': l[pos], q = '1', 3
    
    return f(pos-1, l, q)


print(int(f(sp, list(n), 1), 2))
