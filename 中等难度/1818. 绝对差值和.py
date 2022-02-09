def minAbsoluteSumDiff(nums1: [int], nums2: [int]) -> int:
    def quick_sort(left: int, right: int) -> None:
        if left < right:
            i = left
            j = right
            pivot1 = nums1[left]
            pivot2 = nums2[left]
            while i != j:
                while j > i and nums1[j] > pivot1:
                    j -= 1
                if j > i:
                    nums1[i] = nums1[j]
                    nums2[i] = nums2[j]
                    i += 1
                while i < j and nums1[i] < pivot1:
                    i += 1
                if i < j:
                    nums1[j] = nums1[i]
                    nums2[j] = nums2[i]
                    j -= 1
            nums1[i] = pivot1
            nums2[i] = pivot2
            quick_sort(left, i - 1)
            quick_sort(i + 1, right)

    def search(target: int, leng: int) -> int:
        L, R = 0, leng - 1
        while L < R:
            m = L + (R - L) // 2
            if nums1[m] > target:
                R = m - 1
            elif nums1[m] < target:
                L = m + 1
            elif nums1[m] == target:
                return target
        if abs(target-nums1[L]) < abs(nums1[R]-target):
            return nums1[L]
        return nums1[R]

    n = nums1.__len__()
    quick_sort(0, n-1)
    asd = 0
    maxs = []
    for num1, num2 in zip(nums1, nums2):
        diff = abs(num1 - num2)
        asd += diff
        m = search(num2, n)
        maxs.append(diff-abs(m - num2))
    return (asd - max(maxs)) % 1000000007


if __name__ == '__main__':
    print(minAbsoluteSumDiff(nums1=[1, 7, 5], nums2=[2, 3, 5]))
    print(minAbsoluteSumDiff(nums1=[2, 4, 6, 8, 10], nums2=[2, 4, 6, 8, 10]))
    print(minAbsoluteSumDiff(nums1=[1, 10, 4, 4, 2, 7], nums2=[9, 3, 5, 1, 7, 4]))
