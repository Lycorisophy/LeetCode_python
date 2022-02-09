def deleteAndEarn(nums: [int]) -> int:
    m = max(nums)
    total = [0] * (m + 1)
    for num in nums:
        total[num] += num

    def rob(arrs: [int]) -> int:
        size = len(arrs)
        first, second = arrs[0], max(arrs[0], arrs[1])
        for i in range(2, size):
            first, second = second, max(first + arrs[i], second)
        return second

    return rob(total)


if __name__ == '__main__':
    print(deleteAndEarn([3, 4, 2]))
    print(deleteAndEarn([2, 2, 3, 3, 3, 4]))
