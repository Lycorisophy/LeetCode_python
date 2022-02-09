def nextPermutation(nums: [int]) -> None:
    def quick_sort(nums: list, left: int, right: int) -> None:
        if left < right:
            i = left
            j = right
            pivot = nums[left]
            while i != j:
                while j > i and nums[j] > pivot:
                    j -= 1
                if j > i:
                    nums[i] = nums[j]
                    i += 1
                while i < j and nums[i] < pivot:
                    i += 1
                if i < j:
                    nums[j] = nums[i]
                    j -= 1
            nums[i] = pivot
            quick_sort(nums, left, i - 1)
            quick_sort(nums, i + 1, right)
    n = nums.__len__()
    if n > 1:
        has_change = False
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            has_change = True
            quick_sort(nums, i+1, n-1)
        if not has_change:
            nums.sort()
    return nums


if __name__ == '__main__':
    print(nextPermutation([5,4,7,5,3,2]))
    print(nextPermutation([3, 2, 1]))
    print(nextPermutation([1, 1, 5]))
    print(nextPermutation([1, 2]))
