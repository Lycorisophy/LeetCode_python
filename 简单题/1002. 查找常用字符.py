from collections import Counter
from functools import reduce


# def commonChars(A: [str]) -> [str]:
#     def intersect(nums1, nums2):
#         list1 = set(nums1) & set(nums2)
#         n = []
#         for i in list1:
#             n += [i] * min(nums1.count(i), nums2.count(i))
#         return n
#
#     return reduce(intersect, A)


def commonChars(A: [str]) -> [str]:
    res = []
    for i in reduce(lambda x, y: set(x) & set(y), A):
        res += [i] * reduce(lambda x, y: min(x, y.count(i)), [A[0].count(i)] + A[1:])
    return res


if __name__ == '__main__':
    print(commonChars(["bella", "label", "roller"]))
    print(commonChars(["cool", "lock", "cook"]))
