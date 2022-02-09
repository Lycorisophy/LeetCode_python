def getMaximumGenerated(n: int) -> int:
    indexs = [0, 1, 3, 5, 9, 11, 19, 21, 35, 37, 43, 69, 73, 75, 83, 85, 100]
    keys = [0, 1, 2, 3, 4, 5, 7, 8, 9, 11, 13, 14, 15, 18, 19, 21, 21]
    for i, index in enumerate(indexs):
        if n == index:
            return keys[i]
        elif n < index:
            return keys[i-1]


if __name__ == '__main__':
    print(getMaximumGenerated(100))
