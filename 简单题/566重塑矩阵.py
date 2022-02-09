def matrixReshape(nums: [[int]], r: int, c: int) -> [[int]]:
    nr, nc = len(nums), len(nums[0])
    if r * c != nr * nc:
        return nums
    res = [[0] * c for _ in range(r)]
    count = 0
    for i in range(r):
        for j in range(c):
            x = count // nc
            y = count - nc * x
            res[i][j] = nums[x][y]
            count += 1
    return res


if __name__ == '__main__':
    print(matrixReshape([[1,2,3,4]]
,2
,2))

