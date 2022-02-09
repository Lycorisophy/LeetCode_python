def constructRectangle(area: int) -> [int]:
    root = int(area**(1/2))
    for L in range(root, 0, -1):
        if area % L == 0:
            return [int(area//L), L]


if __name__ == '__main__':
    print(constructRectangle(1))
    print(constructRectangle(16))
    print(constructRectangle(99))
    print(constructRectangle(256))
    print(constructRectangle(137))
