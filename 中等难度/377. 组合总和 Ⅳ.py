def combinationSum4(nums: [int], target: int) -> int:
    if not nums:
        return 0
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i - num]
    return dp[target]


if __name__ == '__main__':
    print(combinationSum4(nums = [1,2,3], target = 4))
    print(combinationSum4(nums = [9], target = 3))

