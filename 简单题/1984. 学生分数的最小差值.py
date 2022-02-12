def minimumDifference(nums: [int], k: int) -> int:
    if k == 1:
        return 0
    sorted_nums = nums.copy()
    sorted_nums.sort()
    n = sorted_nums.__len__()
    res = sorted_nums[n-1] - sorted_nums[0]
    i, j = 0, k-1
    while j < n:
        res = min(sorted_nums[j]-sorted_nums[i], res)
        i += 1
        j += 1
    return res


if __name__ == '__main__':
    print(minimumDifference(nums=[90], k=1))
    print(minimumDifference(nums=[9, 4, 1, 7], k=2))
    print(minimumDifference(nums=[9, 4, 1, 7], k=3))
    print(minimumDifference(nums=[9, 4, 1, 7], k=4))
