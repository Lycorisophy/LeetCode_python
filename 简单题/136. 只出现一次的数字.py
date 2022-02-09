from functools import reduce


def singleNumber(nums: [int]) -> int:
    return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    print(singleNumber([2, 2, 1]))
    print(singleNumber([4, 1, 2, 1, 2]))
