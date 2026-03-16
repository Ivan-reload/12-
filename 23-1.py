def f(n, k):
    if n in (24, 32):
        k += 1
    if n == 48 and k == 1:
        return 1
    elif n > 48 or k > 1:
        return 0
    else:
        return f(n+1, k) + f(n+2, k) + f(n+4, k) + f(n+8, k)

print(f(16, 0))
