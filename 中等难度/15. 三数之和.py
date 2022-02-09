def threeSum(nums: [int]) -> [[int]]:
    n = nums.__len__()
    if n < 3:
        return []
    nums.sort()
    res = []
    for i, num in enumerate(nums):
        if num > 0:
            return res
        if i > 0 and num == nums[i - 1]:
            continue
        L = i + 1
        R = n - 1
        while L < R:
            s = num + nums[L] + nums[R]
            if s == 0:
                res.append([num, nums[L], nums[R]])
                while L < R and nums[L] == nums[L + 1]:
                    L = L + 1
                while L < R and nums[R] == nums[R - 1]:
                    R = R - 1
                L = L + 1
                R = R - 1
            elif s > 0:
                R = R - 1
            else:
                L = L + 1
    return res


if __name__ == '__main__':
    print(threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
    print(threeSum([1,0,-1,-2,1,4]))
    print(threeSum([0]))
