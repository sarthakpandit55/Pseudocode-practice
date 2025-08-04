def mystery(a, b):
    if (b == 0):
        return 0
    return a + mystery(a, (b-1))
print(mystery(3,4))