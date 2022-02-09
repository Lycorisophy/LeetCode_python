# 给定两个数组，编写一个函数来计算它们的交集。


def intersection(nums1: [int], nums2: [int]) -> [int]:
    nums3 = []
    for i, data in enumerate(nums1):
        if data in nums2 and data not in nums3:
            nums3.append(data)
    return nums3


if __name__ == '__main__':
    print(intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
