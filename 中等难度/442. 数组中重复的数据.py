def findDuplicates(nums: [int]) -> [int]:
    n = nums.__len__()
    res = set(nums)
    for i in range(n):
        nums[abs(nums[i])-1] *= -1
    for i, num in enumerate(nums):
        if num < 0:
            res.remove(i+1)
    return list(res)


if __name__ == '__main__':
    print(findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
