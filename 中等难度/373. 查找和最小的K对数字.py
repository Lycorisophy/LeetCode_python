import itertools
import heapq


def kSmallestPairs(nums1: [int], nums2: [int], k: int) -> [[int]]:
    streams = map(lambda u: ([u + v, u, v] for v in nums2), nums1)
    stream = heapq.merge(*streams)
    return [suv[1:] for suv in itertools.islice(stream, k)]


if __name__ == '__main__':
    print(kSmallestPairs(nums1=[1, 2, 4], nums2=[-1, 1, 2], k=100))
    print(kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2))
    print(kSmallestPairs(nums1=[1, 2], nums2=[3], k=3))
