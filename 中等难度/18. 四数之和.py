def fourSum(nums: [int], target: int) -> [[int]]:
    n = nums.__len__()
    if n < 4:
        return []
    nums.sort()
    res = []
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break
        if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break
            if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                continue
            L, R = j + 1, n - 1
            while L < R:
                total = nums[i] + nums[j] + nums[L] + nums[R]
                if total == target:
                    res.append([nums[i], nums[j], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    R -= 1
                elif total < target:
                    L += 1
                else:
                    R -= 1
    return res



if __name__ == '__main__':
    print(fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
    print(fourSum(nums=[], target=0))
