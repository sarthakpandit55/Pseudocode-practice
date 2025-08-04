a = 10
def test():
    global a
    a = a + 5
test()
print(a)

# output = 15