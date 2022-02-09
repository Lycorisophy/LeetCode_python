def wiggleMaxLength(nums: [int]) -> int:
    n = len(nums)
    if n < 2:
        return n

    up = [1] + [0] * (n - 1)
    down = [1] + [0] * (n - 1)
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            up[i] = max(up[i - 1], down[i - 1] + 1)
            down[i] = down[i - 1]
        elif nums[i] < nums[i - 1]:
            up[i] = up[i - 1]
            down[i] = max(up[i - 1] + 1, down[i - 1])
        else:
            up[i] = up[i - 1]
            down[i] = down[i - 1]

    return max(up[n - 1], down[n - 1])


if __name__ == '__main__':
    print(wiggleMaxLength([1,7,4,9,2,5]))
    print(wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
    print(wiggleMaxLength([1,2,3,4,5,6,7,8,9]))
