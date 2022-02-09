def integerReplacement(n: int) -> int:
    cnt = 0
    while n != 1:
        if (n & 1) == 0:
            n >>= 1
        else:
            n += -1 if (n & 2) == 0 or n == 3 else 1
        cnt += 1
    return cnt


if __name__ == '__main__':
    print(integerReplacement(7))
    print(integerReplacement(7))
    print(integerReplacement(4))
    print(integerReplacement(2**31-1))