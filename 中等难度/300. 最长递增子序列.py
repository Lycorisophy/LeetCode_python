def lengthOfLIS(nums: [int]) -> int:
    n = nums.__len__()
    if n == 1:
        return 1
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        base = nums[i]
        for j in range(i+1):
            if nums[j] < base:
                dp[i] = max(dp[i], dp[j])
        dp[i] += 1
    return max(dp)


if __name__ == '__main__':
    print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(lengthOfLIS([0, 1, 0, 3, 2, 3]))
    print(lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
