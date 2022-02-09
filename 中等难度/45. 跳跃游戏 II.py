def jump(nums: [int]) -> int:
    nums = nums[::-1]
    n = nums.__len__()
    dp = [0 for _ in range(n)]
    for i in range(1, n):
        num = nums[i]
        if num == 0:
            dp[i] = n
        else:
            min_step = n
            for j in range(max(i - num, 0), i):
                step = dp[j]
                if step <= min_step:
                    min_step = step
            dp[i] = min_step + 1
    return dp[-1]


if __name__ == '__main__':
    print(jump([1, 1, 7, 5, 8, 4]))
    print(jump([2, 3, 0, 1, 4]))
