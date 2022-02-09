def luckyNumbers(matrix: [[int]]) -> [int]:
    def getMin(arr: [int]):
        minVal, index = 10**5, 0
        for i, v in enumerate(arr):
            if v < minVal:
                index = i
                minVal = v
        return index, minVal

    res = []
    minList = {}
    for row in matrix:
        index, minVal = getMin(row)
        if index not in minList:
            minList[index] = minVal
        else:
            minList[index] = max(minList[index], minVal)
    matrix = list(zip(*matrix))
    for key, val in minList.items():
        if val == max(matrix[key]):
            res.append(val)
    return res


if __name__ == '__main__':
    print(luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
    print(luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
    print(luckyNumbers([[7, 8], [1, 2]]))
