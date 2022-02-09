def maxArea(height: [int]) -> int:
    n = height.__len__()
    i, j, res = 0, n - 1, 0
    while i < j:
        a, b = height[i], height[j]
        if a < b:
            res = max(res, a * (j - i))
            i += 1
        else:
            res = max(res, b * (j - i))
            j -= 1
    return res


if __name__ == '__main__':
    print(maxArea([1,8,6,2,5,4,8,3,7]))
    print(maxArea([1,1]))
    print(maxArea([4,3,2,1,4]))
    print(maxArea([1,2,1]))
