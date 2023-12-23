# ////معکوس کردن عدد////
def invert(num):
    return int(str(num)[::-1])
# ////sigma//////جمع عدد با عدد های قبل از خودش
def sigma(n):
    if n == 1:
        return 1
    return sigma(n-1) + n
# ////جمع مجموع عدد های هر عدد الی اخر/////
def numsum(n):
    if n < 10:
        return n
    s = 0
    for i in str(n):
        s += int(i)
    return numsum(s)
invert(51)
# ///15///
print(sigma(51))
# ///1326////
numsum(51)
# ///6///