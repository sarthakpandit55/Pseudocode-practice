def fun(n):
    if(n <= 1):
        return n
    return fun(n-1) + fun(n-3)
print(fun(5))