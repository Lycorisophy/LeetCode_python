def sortArrayByParity(A: [int]) -> [int]:
    def quick_sort(nums: list, i: int, j: int) -> None:
        if i < j:
            while i != j:
                while j > i and nums[j] % 2 == 1:
                    j -= 1
                while i < j and nums[i] % 2 == 0:
                    i += 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            quick_sort(nums, i, j-1)

    quick_sort(A, 0, A.__len__() - 1)
    return A


if __name__ == '__main__':
    print(sortArrayByParity([3, 1, 2, 4, 94, 123, 546, 865, 2341, 75]))
