def generate(numRows: int) -> [[int]]:
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]
    lastRows = generate(numRows - 1)
    lastRow = lastRows[numRows-2]
    nextRow = [1] * numRows
    for i in range(1, numRows-1):
        nextRow[i] = lastRow[i] + lastRow[i-1]
    lastRows.append(nextRow)
    return lastRows


if __name__ == '__main__':
    print(generate(5))
    print(generate(8))
