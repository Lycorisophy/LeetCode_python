from collections import Counter
from functools import reduce


def hasGroupsSizeX(deck: [int]) -> bool:
    def gcd(x, y):
        if x % y == 0:
            return y
        return gcd(y, x % y)

    counter = list(set(dict(Counter(deck)).values()))
    return reduce(gcd, counter) >= 2


if __name__ == '__main__':
    print(hasGroupsSizeX([1, 2]))
    print(hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3, 1, 3,1,1]))
    print(hasGroupsSizeX([1, 1, 2, 2, 2, 2]))
