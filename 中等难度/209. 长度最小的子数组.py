def minSubArrayLen(target: int, nums: [int]) -> int:
    n = nums.__len__()
    res = n + 1
    start, end = 0, 0
    total = 0
    while end < n:
        total += nums[end]
        while total >= target:
            res = min(res, end - start + 1)
            total -= nums[start]
            start += 1
        end += 1
    return res if res != n + 1 else 0


if __name__ == '__main__':
    print(minSubArrayLen(target=4, nums=[1, 4, 4]))
    print(minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
    print(minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
