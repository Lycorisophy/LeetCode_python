def findPeakElement(nums: [int]) -> int:
    n = nums.__len__()
    if n == 1:
        return 0
    i, j = 0, n-1
    while i < j:
        if nums[i] > nums[i+1]:
            return i
        if nums[j] > nums[j-1]:
            return j
        pre = nums[i]
        for k in range(i+1, j):
            if nums[k] > pre:
                i = k
                break
            else:
                pre = nums[k]
        pre = nums[j]
        for k in range(j-1, i, -1):
            if nums[k] > pre:
                j = k
                break
            else:
                pre = nums[k]
    return -1


if __name__ == '__main__':
    print(findPeakElement([1, 2, 3, 1]))
    print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))
    print(findPeakElement([1]))
