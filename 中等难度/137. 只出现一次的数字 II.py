def singleNumber(nums: [int]) -> int:
    a = b = 0
    for num in nums:
        b = ~a & (b ^ num)
        a = ~b & (a ^ num)
    return b


if __name__ == '__main__':
    print(singleNumber([2, 2, 3, 2]))
    print(singleNumber([0, 1, 0, 1, 0, 1, 99]))
