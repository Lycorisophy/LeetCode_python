def countNegatives(grid: [[int]]) -> int:
    res = 0
    for arr in grid:
        do_plus = False
        for i, a in enumerate(arr):
            if a < 0:
                do_plus = True
                break
        if do_plus:
            res += arr.__len__() - i
    return res


if __name__ == '__main__':
    print(countNegatives(grid=[[5, 1, 0], [-5, -5, -5]]))
    print(countNegatives(grid=[[3, 2], [1, 0]]))
    print(countNegatives(grid=[[1, -1], [-1, -1]]))
    print(countNegatives(grid=[[-1]]))
