def seaRchRange(nums: [int], target: int) -> [int]:
    n = nums.__len__()
    L, R = 0, n - 1
    while L <= R:
        m = L + (R - L) // 2
        if nums[m] > target:
            R = m - 1
        elif nums[m] < target:
            L = m + 1
        elif nums[m] == target:
            break
    else:
        return [-1, -1]
    L, R = m-1, m+1
    while L >= 0:
        if nums[L] == target:
            L -= 1
        else:
            break
    while R < n:
        if nums[R] == target:
            R += 1
        else:
            break
    return [L+1, R-1]


if __name__ == '__main__':
    print(seaRchRange(nums = [5,7,7,8,8,10], target = 8))
    print(seaRchRange(nums = [5,7,7,8,8,10], target = 6))
    print(seaRchRange(nums = [], target = 0))
