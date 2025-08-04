def recUpdate(a):
    if a > 10:
        return a
    return recUpdate(a + 2)
print(recUpdate(4))