def isPowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False
    n = bin(n)
    num = 0
    for i, data in enumerate(n):
        if data == '1':
            num += 1
            if num == 2:
                return False
    return True


if __name__ == '__main__':
    print(isPowerOfTwo(0))