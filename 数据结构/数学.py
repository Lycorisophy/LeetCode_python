# 最大公约数
def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)
