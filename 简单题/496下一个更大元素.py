def nextGreaterElement(nums1: [int], nums2: [int]) -> [int]:
    l1, l2 = len(nums1), len(nums2)
    m = {}
    r = []
    for n2 in nums2:
        m[n2] = -1
    for i in range(l2):
        pass
    for j in range(l1):
        r.append(m[nums1[j]])
    return r


if __name__ == '__main__':
    print(nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
    print(nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4]))
