def rob(nums: [int]) -> int:
    n = nums.__len__()
    if n < 3:
        return max(nums)
    dp = nums.copy()
    i = 2
    while i < n:
        dp[i] += max(dp[:i-1])
        i += 1
    return max(dp)


if __name__ == '__main__':
    print(rob([1, 2, 3, 1]))
    print(rob([2, 7, 9, 3, 1]))
    print(rob([2, 7, 9, 3, 11, 1, 3, 99, 1]))
