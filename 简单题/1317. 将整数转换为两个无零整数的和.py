import random


def getNoZeroIntegers(n: int) -> [int]:
    if n < 1000:
        i = 1
        while i < n:
            j = n - i
            if '0' not in str(i) and '0' not in str(j):
                return [i, j]
            i += 1
    while True:
        i = random.randint(1, n)
        j = n - i
        if '0' not in str(i) and '0' not in str(j):
            return [i, j]


if __name__ == '__main__':
    print(getNoZeroIntegers(10909))

