def canJump(nums: [int]) -> bool:
    nums = nums[::-1]
    n = nums.__len__()
    dp = [False for _ in range(n)]
    dp[0] = True
    for i in range(1, n):
        num = nums[i]
        if num == 0:
            pass
        else:
            for j in range(max(i - num, 0), i):
                if dp[j]:
                    dp[i] = True
                    break
    return dp[-1]


if __name__ == '__main__':
    print(canJump([2, 3, 1, 1, 4]))
    print(canJump([3, 2, 1, 0, 4]))
    print(canJump([2, 3, 0, 1, 4]))
