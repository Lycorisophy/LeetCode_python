def search(nums: [int], target: int) -> bool:
    n = nums.__len__()
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        num = nums[mid]
        if num == target:
            return True
        if nums[l] == nums[mid] and nums[mid] == nums[r]:
            l += 1
            r -= 1
        elif nums[l] <= nums[mid]:
            if nums[l] <= target and target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target and target <= nums[n - 1]:
                l = mid + 1
            else:
                r = mid - 1
    return False


if __name__ == '__main__':
    print(search([2, 5, 6, 0, 0, 1, 2], 0))
    print(search([2, 5, 6, 0, 0, 1, 2], 3))
    print(search([2, 5, 6, 0, 0, 1, 2], 5))
    print(search([2, 5, 6, 0, 0, 1, 2], 7))
    print(search([2, 5, 6, 0, 0, 1, 2], -7))
    print(search([2], 2))
