from functools import lru_cache


@lru_cache
def simplifiedFractions(n: int) -> [str]:
    if n == 1:
        return []
    if n == 2:
        return ["1/2"]
    else:
        str_n = str(n)
        res = ["1/"+str_n]
        for i in range(2, n):
            if gcd(n, i) == 1:
                res.append(str(i)+"/"+str_n)
        return res + simplifiedFractions(n-1)


def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)


if __name__ == '__main__':
    print(simplifiedFractions(1))
    print(simplifiedFractions(2))
    print(simplifiedFractions(3))
    print(simplifiedFractions(4))
    print(simplifiedFractions(5))
    print(simplifiedFractions(6))
