from collections import Counter


def numIdenticalPairs(nums: [int]) -> int:
    cnt = Counter(nums)
    res = 0
    for v in cnt.values():
        if v > 1:
            res += v*(v-1)//2
    return res


if __name__ == '__main__':
    print(numIdenticalPairs([1, 2, 3, 1, 1, 3]))
    print(numIdenticalPairs([1, 1, 1, 1]))
    print(numIdenticalPairs([1, 2, 3]))
