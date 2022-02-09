def findTargetSumWays(nums: [int], target: int) -> int:
    # n = len(nums)
    #
    # def backtrack(tmp, index):
    #     if index == n:
    #         if tmp == target:
    #             return 1
    #         return 0
    #     return backtrack(tmp + nums[index], index + 1) + backtrack(tmp - nums[index], index + 1)
    #
    # return backtrack(0, 0)
    target = abs(target)
    sumAll = sum(nums)
    if target > sumAll or (target + sumAll) % 2:
        return 0
    target = (target + sumAll) // 2

    dp = [0] * (target + 1)
    dp[0] = 1

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] + dp[j - num]
    return dp[-1]


if __name__ == '__main__':
    print(findTargetSumWays([100], -200))
    print(findTargetSumWays([1, 1, 2, 1, 1], 6))
    print(findTargetSumWays([1, 1, 2, 1, 1, 3, 4, 5], 12))
