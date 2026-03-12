n = ''.zfill(151)

def f(pos, l, q):
    if pos == 151:
        return l.count('1')
    
    n = l[pos]
    if q == 1:
        if n == '0': l[pos], q = '0', 3
        elif n == '1': l[pos], q = '1', 2
    
    elif q == 2:
        if n == '0': l[pos], q = '1', 3
        elif n == '1': l[pos], q = '0', 3
    
    elif q == 3:
        if n == '0': l[pos], q = '0', 2
        elif n == '1': l[pos], q = '1', 2
    
    return f(pos+1, l, q)


print(f(0, list(n), 1))
