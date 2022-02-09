def threeSumClosest(nums: [int], target: int) -> int:
    n = nums.__len__()
    nums.sort()
    res = nums[0] + nums[1] + nums[2]
    for i, num in enumerate(nums):
        L = i + 1
        R = n - 1
        while L < R:
            s = num + nums[L] + nums[R]
            if s == target:
                return target
            elif s > target:
                R = R - 1
                if s - target < abs(res-target):
                    res = s
            else:
                L = L + 1
                if target - s < abs(res-target):
                    res = s
    return res


if __name__ == '__main__':
    print(threeSumClosest(nums=[-100,-98,-2,-1]
, target=-101))
    print(threeSumClosest(nums=[-1, 2, 1, 1, -4, 8, 12, 63], target=15))
    print(threeSumClosest(nums=[-1, 2, 1, -4, 8, 12, 63, 56, 2315, 235, 76], target=123456))
