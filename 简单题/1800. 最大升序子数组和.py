def maxAscendingSum(nums: [int]) -> int:
    max_sum = 1
    num_sum = 0
    pre = 0
    for num in nums:
        if num > pre:
            num_sum += num
        else:
            if num_sum > max_sum:
                max_sum = num_sum
            num_sum = num
        pre = num
    if num_sum > max_sum:
        return num_sum
    return max_sum


if __name__ == '__main__':
    print(maxAscendingSum([10, 20, 30, 5, 10, 50]))
    print(maxAscendingSum([10, 20, 30, 40, 50]))
    print(maxAscendingSum([12, 17, 15, 13, 10, 11, 12]))
    print(maxAscendingSum([100, 10, 1]))
