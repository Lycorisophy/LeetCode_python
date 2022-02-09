def grayCode(n: int) -> [int]:
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    lastCode = grayCode(n-1)
    return lastCode + [1 << (n - 1) | x for x in lastCode[::-1]]


if __name__ == '__main__':
    print(grayCode(2))
    print(grayCode(3))
    print(grayCode(4))
    print(grayCode(5))
