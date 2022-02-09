def minSubsequence(nums: [int]) -> [int]:
    nums.sort(reverse=True)
    s = sum(nums)
    subSum = 0
    res = []
    for num in nums:
        subSum += num
        res.append(num)
        if subSum * 2 > s:
            return res


if __name__ == '__main__':
    print(minSubsequence([4, 3, 10, 9, 8]))
    print(minSubsequence([4, 4, 7, 6, 7]))
    print(minSubsequence([6]))
