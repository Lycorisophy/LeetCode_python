from functools import reduce


def singleNumber(nums: [int]) -> [int]:
    ret = reduce(lambda x, y: x ^ y, nums)
    div = 1
    while div & ret == 0:
        div <<= 1
    a, b = 0, 0
    for n in nums:
        if n & div:
            a ^= n
        else:
            b ^= n
    return [a, b]


if __name__ == '__main__':
    print(singleNumber([1, 2, 1, 3, 2, 5]))
    print(singleNumber([5, 2, 3, 1, 2, 1]))
    print(singleNumber([1, 2, 1, 3, 5, 2]))
    print(singleNumber([2, 5, 3, 1, 2, 1]))
    print(singleNumber([-1, 0]))
    print(singleNumber([0, 1]))
