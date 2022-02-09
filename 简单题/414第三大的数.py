def thirdMax(nums: [int]) -> int:
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return nums[0] if nums[0] > nums[1] else nums[1]
    else:
        import math
        res = [-math.inf]*3
        for num in nums:
            if num > res[2]:
                res[0] = res[1]
                res[1] = res[2]
                res[2] = num
            elif num > res[1] and num < res[2]:
                res[0] = res[1]
                res[1] = num
            elif num > res[0] and num < res[1]:
                res[0] = num
        if res[0] != -math.inf:
            return res[0]
        else:
            return res[2]


if __name__ == '__main__':
    print(thirdMax([1, 1, 2]))