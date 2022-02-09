def binarySearch(arr, l, r, x):
    # 基本判断
    if r >= l:

        mid = int(l + (r - l) / 2)

        # 元素整好的中间位置
        if arr[mid] == x:
            return mid

            # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

            # 元素大于中间位置的元素，只需要再比较右边的元素
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # 不存在
        return -1


# 二分查找
def search(nums: [int], target: int) -> int:
    L, R = 0, len(nums)-1
    while L <= R:
        m = L + (R - L) // 2
        if nums[m] > target:
            R = m - 1
        elif nums[m] < target:
            L = m + 1
        elif nums[m] == target:
            return m
    return -1
