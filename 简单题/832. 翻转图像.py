def flipAndInvertImage(image: [[int]]) -> [[int]]:
    r = lambda v: 1 - v
    return [[r(v) for v in row[::-1]] for row in image]


if __name__ == '__main__':
    print(flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
    print(flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
    print(flipAndInvertImage([[0]]))
