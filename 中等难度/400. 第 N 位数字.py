def findNthDigit(n: int) -> int:
    if n == 0:
        return 0
    digit = 1
    start = 1
    index_count = digit * 9 * start
    while n > index_count:
        n -= index_count
        digit += 1
        start *= 10
        index_count = digit * 9 * start
    num = start + (n - 1) // digit
    remainder = (n - 1) % digit
    s_num = str(num)
    return int(s_num[remainder])


if __name__ == '__main__':
    print(findNthDigit(11))
