def numberOfArithmeticSlices(nums: [int]) -> int:
    n = len(nums)
    if n < 3:
        return 0
    dp = [0] * (n-1)
    if nums[2] + nums[0] - 2*nums[1] == 0:
        dp[1] = 1
    for i in range(3, n):
        base = dp[i-2]
        dp[i - 1] = base
        if nums[i] + nums[i-2] - 2*nums[i-1] == 0:
            add = 1
            for j in range(i-3, -1, -1):
                if dp[j] == base:
                    break
                else:
                    add += 1
            dp[i-1] += add
    return dp[-1]


if __name__ == '__main__':
    print(numberOfArithmeticSlices([1, 2, 3]))
    print(numberOfArithmeticSlices([1, 2, 3, 4]))
    print(numberOfArithmeticSlices([1]))
