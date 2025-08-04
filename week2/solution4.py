def fun(x):
    if x == 0:
        return
    fun(x-1)
    print(x)
fun(3)