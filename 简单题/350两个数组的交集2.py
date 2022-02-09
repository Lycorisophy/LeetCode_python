# 给定两个数组，编写一个函数来计算它们的交集。


def intersect(nums1: [int], nums2: [int]) -> [int]:
    if nums1 == [] or nums2 == []:
        return []
    l1, l2 = len(nums1), len(nums2)
    if l1 > l2:
        nums1, nums2 = nums2, nums1
        l1, l2 = l2, l1
    i = 0
    nums = []
    while i < l2:
        for j in range(l1):
            if nums1[j] != nums2[i]:
                i += 1
                if nums != []:
                    return nums
                break
            else:
                i += 1
                nums.append(nums1[j])
    return nums



if __name__ == '__main__':
    print(intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
