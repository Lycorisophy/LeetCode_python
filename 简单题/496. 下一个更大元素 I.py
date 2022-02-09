from collections import defaultdict


def nextGreaterElement(nums1: [int], nums2: [int]) -> [int]:
    maxNum = -1
    arrs = list()
    nextGreaterElementDict = defaultdict()
    for num in nums2[::-1]:
        if num > maxNum:
            nextGreaterElementDict[num] = -1
            maxNum = num
            arrs = [num]
        else:
            for arr in arrs:
                if arr > num:
                    nextGreaterElementDict[num] = arr
                    break
            arrs = [num] + arrs
    res = [0] * len(nums1)
    for i, num in enumerate(nums1):
        res[i] = nextGreaterElementDict[num]
    return res


if __name__ == '__main__':
    print(nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
    print(nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]))
