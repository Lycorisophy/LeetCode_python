# 颠倒给定的 32 位无符号整数的二进制位。


def reverseBits(n: int) -> int:
    n = bin(n)
    for i, data in enumerate(n):
        print(data)
    return 1


if __name__ == '__main__':
    print(reverseBits(43261596))