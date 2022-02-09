def maximumUnits(boxTypes: [[int]], truckSize: int) -> int:
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    res = 0
    for numberOfBoxes, numberOfUnitsPerBox in boxTypes:
        if numberOfBoxes < truckSize:
            res += numberOfBoxes * numberOfUnitsPerBox
            truckSize -= numberOfBoxes
        else:
            res += truckSize * numberOfUnitsPerBox
            return res
    return res


if __name__ == '__main__':
    print(maximumUnits(boxTypes=[[1, 3], [2, 2], [3, 1]], truckSize=4))
    print(maximumUnits(boxTypes=[[5, 10], [2, 5], [4, 7], [3, 9]], truckSize=10))
