def findKthLargest(nums: [int], k: int) -> int:
    n = nums.__len__()
    for i in range(k):
        for j in range(n-1, i, -1):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums[k-1]


if __name__ == '__main__':
    print(findKthLargest([3,2,1,5,6,4], 2))
    print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))

