def searchInsert(nums: [int], target: int) -> int:
    def binarySearch(arr, l, r, x):
        if r >= l:
            mid = int(l + (r - l) / 2)
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return binarySearch(arr, l, mid - 1, x)
            return binarySearch(arr, mid + 1, r, x)
        arr.insert(l, target)
        return l
    return binarySearch(nums, 0, len(nums)-1, target)


if __name__ == '__main__':
    nums = [1,3,5,6]
    nums3 = [1,3,5,6]
    nums2 = []
    print(searchInsert(nums, 5), nums)
    print(searchInsert(nums3, 2), nums3)
    print(searchInsert(nums, 7), nums)
    print(searchInsert(nums2, 0), nums2)
    print(searchInsert(nums2, 0), nums2)

