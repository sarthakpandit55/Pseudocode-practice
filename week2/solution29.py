x = 1
def outer():
    x = 2
    def inner():
        print(x)
    inner()
outer()

# output = 2

