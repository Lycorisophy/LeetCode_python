import math


def bulbSwitch(n: int) -> int:
    if n < 6:
        if n == 0:
            return 0
        elif n < 4:
            return 1
        else:
            return 2
    low = 1
    up = n // 2 + 1
    while True:
        mid = (low + up) // 2
        m = mid ** 2
        if m == n:
            return mid
        elif m > n:
            if (m + 1 - 2 * mid) < n:
                return mid - 1
            up = mid
        else:
            low = mid


if __name__ == '__main__':
    for i in range(1000):
        print(bulbSwitch(i))

