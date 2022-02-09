def heightChecker(heights: [int]) -> int:
    res = 0
    sorted_height = heights.copy()
    sorted_height.sort()
    for a, b in zip(sorted_height, heights):
        if a != b:
            res += 1
    return res



if __name__ == '__main__':
    print(heightChecker([1, 1, 4, 2, 1, 3]))
    print(heightChecker([5, 1, 2, 3, 4]))
    print(heightChecker([1, 2, 3, 4, 5]))
