def sortArrayByParityII(nums: [int]) -> [int]:
    l = nums.__len__()

    def quick_sort(ns: list, i: int, j: int, n: int) -> None:
        while i < n and j < n:
            if ns[i] % 2 == 0:
                i += 2
                if ns[j] % 2 == 1:
                    j += 2
            else:
                if ns[j] % 2 == 1:
                    j += 2
                else:
                    ns[i], ns[j] = ns[j], ns[i]
                    i += 2
                    j += 2

    quick_sort(nums, 0, 1, l)
    return nums


if __name__ == '__main__':
    print(sortArrayByParityII([4, 2, 5, 7, 2, 9]))

