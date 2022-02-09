def restoreString(s: str, indices: [int]) -> str:
    def quick_sort(nums: list, strs: list, left: int, right: int):
        if left < right:
            i = left
            j = right
            pivot = nums[left]
            tmp = strs[left]
            while i != j:
                while j > i and nums[j] > pivot:
                    j -= 1
                if j > i:
                    nums[i] = nums[j]
                    strs[i] = strs[j]
                    i += 1
                while i < j and nums[i] < pivot:
                    i += 1
                if i < j:
                    nums[j] = nums[i]
                    strs[j] = strs[i]
                    j -= 1
            nums[i] = pivot
            strs[i] = tmp
            quick_sort(nums, strs, left, i - 1)
            quick_sort(nums, strs, i + 1, right)

    s = list(s)
    quick_sort(indices, s, 0, indices.__len__()-1)
    return ''.join(s)


if __name__ == '__main__':
    print(restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
    print(restoreString(s = "abc", indices = [0,1,2]))
    print(restoreString(s = "aiohn", indices = [3,1,4,2,0]))
