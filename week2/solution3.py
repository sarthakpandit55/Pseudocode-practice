def f(n):
    if n == 0:
        return 0
    else:
        return n + f(n-2)

print(f(6))