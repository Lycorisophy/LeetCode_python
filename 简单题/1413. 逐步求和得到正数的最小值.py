def minStartValue(nums: [int]) -> int:
    nums_sum, local_min = 0, 0
    for num in nums:
        nums_sum += num
        local_min = min(local_min, nums_sum)
    return 1 - local_min


if __name__ == '__main__':
    print(minStartValue([-3, 2, -3, 4, 2]))
    print(minStartValue([1, 2]))
    print(minStartValue([1, -2, -3]))
