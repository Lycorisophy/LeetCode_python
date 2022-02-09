def isToeplitzMatrix(matrix: [[int]]) -> bool:
    base = matrix[0][:-1]
    for i in range(1, 20):
        try:
            if base != matrix[i][1:]:
                return False
            base = matrix[i][:-1]
        except IndexError:
            break
    return True


if __name__ == '__main__':
    print(isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2],[0,9,9,1]]))

