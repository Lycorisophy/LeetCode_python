def numMovesStones(a: int, b: int, c: int) -> [int]:
    arrs = [a, b, c]
    arrs.sort()
    a, b, c = arrs
    if a+1 == b:
        if b+1 == c:
            x = 0
            y = 0
        else:
            x = 1
            y = c - b - 1
    elif b+1 == c:
        if a+1 == b:
            x = 0
            y = 0
        else:
            x = 1
            y = b - a - 1
    elif a+2 == b or b+2 == c:
        x = 1
        y = c - a - 2
    else:
        x = 2
        y = c - a - 2
    return [x, y]


if __name__ == '__main__':
    print(numMovesStones(a=1, b=2, c=5))
    print(numMovesStones(a=4, b=3, c=2))
    print(numMovesStones(a=1, b=3, c=100))
