def arrangeCoins(n: int) -> int:
    c = 0
    while True:
        c += 1
        n -= c
        if n == 0:
            return c
        elif n < 0:
            return c - 1


if __name__ == '__main__':
    print(arrangeCoins(7))