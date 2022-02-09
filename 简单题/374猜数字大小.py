def guessNumber(n: int) -> int:
    l = len(str(n))
    i = 0
    while True:
        i += 1
        gap = 10 ** (l-i)
        while guess(n) == -1:
            n -= gap
        while guess(n) == 1:
            n += gap
        if gap == 1:
            break
    return n


def guess(num: int) -> int:
    if pick < num:
        return -1
    elif pick > num:
        return 1
    else:
        return 0


if __name__ == '__main__':
    pick = 3390
    print(guessNumber(n=6719))
