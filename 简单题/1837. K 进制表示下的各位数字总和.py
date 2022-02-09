def sumBase(n: int, k: int) -> int:
    a, b = n, 0
    res = 0
    while a >= k:
        a, b = divmod(a, k)
        res += b
    return res+a


if __name__ == '__main__':
    print(sumBase(n = 100, k = 2))


