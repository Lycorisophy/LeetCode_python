def search(nums: [int], target: int) -> int:
    if not nums:
        return -1
    n = nums.__len__()
    l, r = 0, n - 1
    left = nums[0]
    right = nums[-1]
    while l <= r:
        mid = (l + r) // 2
        num = nums[mid]
        if num == target:
            return mid
        if left <= num:
            if left <= target < num:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if num < target <= right:
                l = mid + 1
            else:
                r = mid - 1
    return -1


if __name__ == '__main__':
    print(search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
    print(search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
    print(search(nums=[1], target=0))
