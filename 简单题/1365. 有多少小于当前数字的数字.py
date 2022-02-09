def smallerNumbersThanCurrent(nums: [int]) -> [int]:
    nums_b = nums.copy()
    nums_b.sort()
    smaller_list = {}
    for i, num in enumerate(nums_b):
        if num not in smaller_list:
            smaller_list[num] = i
    return [smaller_list[num] for num in nums]


if __name__ == '__main__':
    print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
    print(smallerNumbersThanCurrent([6, 5, 4, 8]))
    print(smallerNumbersThanCurrent([7, 7, 7, 7]))
