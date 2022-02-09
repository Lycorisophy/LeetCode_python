def specialArray(nums: [int]) -> int:
    nums.sort()
    if nums[-1] == 0:
        return -1
    n = nums.__len__()
    for i, num in enumerate(nums):
        if num >= 1:
            break
    if i == n - 1:
        return 1
    pre = i
    for i in range(2, n+1):
        for j in range(pre, n):
            if nums[j] >= i:
                break
        if j == n - i:
            return i
        pre = j
    return -1


if __name__ == '__main__':
    print(specialArray([3, 5]))
    print(specialArray([0, 1]))
    print(specialArray([0, 4, 3, 0, 4]))
    print(specialArray([3, 6, 7, 7, 0]))
