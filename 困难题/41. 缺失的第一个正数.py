def firstMissingPositive(nums: [int]) -> int:
    n = nums.__len__()
    m = n + 1
    for i, num in enumerate(nums):
        if num <= 0:
            nums[i] = m
    for i, num in enumerate(nums):
        num = abs(num)
        if num < m:
            t = nums[num-1]
            if t > 0:
                nums[num-1] = 0 - t
    for i, num in enumerate(nums):
        if num > 0:
            return i + 1
    return m


if __name__ == '__main__':
    print(firstMissingPositive(nums=[1, 2, 0]))
    print(firstMissingPositive(nums=[3, 4, -1, 1]))
    print(firstMissingPositive(nums=[7, 8, 9, 11, 12]))
