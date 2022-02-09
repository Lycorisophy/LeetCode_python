def reverse(x: int) -> int:
    if x < 0:
        x *= -1
        res = -1
    else:
        res = 1
    x = int(str(x)[::-1])
    res *= x
    return res if -2147483649 < res < 2147483648 else 0


if __name__ == '__main__':
    print(2**31)

