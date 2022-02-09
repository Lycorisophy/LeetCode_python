def generateMatrix(n: int) -> [[int]]:
    def orchestraLayout(num: int, xPos: int, yPos: int) -> int:
        n = min(xPos, yPos, num - xPos - 1, num - yPos - 1)
        kinds = 0
        kinds += 4 * n * num - 4 * n - 4 * n * (n - 1)
        if n == xPos:
            kinds += yPos - n + 1
        elif n == yPos:
            kinds += (num - 2 * n) * 3 - 3 + num - n - xPos
        elif n == num - xPos - 1:
            kinds += (num - 2 * n) * 2 - 2 + num - n - yPos
        elif n == num - yPos - 1:
            kinds += (num - 2 * n) * 1 - 1 + xPos - n + 1
        return kinds

    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = orchestraLayout(n, i, j)
    return res


if __name__ == '__main__':
    print(generateMatrix(3))
    print(generateMatrix(1))
    print(generateMatrix(5))
