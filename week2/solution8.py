from week1.solution10 import count


def fun(n):
    count = 0
    if(n == 0):
        return
    fun(n-1)
    fun(n-1)
    count += 1
fun(3)
print(count)