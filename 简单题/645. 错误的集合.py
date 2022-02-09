def findErrorNums(nums: [int]) -> [int]:
    existNums = [0] * len(nums)
    for num in nums:
        if existNums[num-1] == 1:
            doubleNum = num
        existNums[num-1] = 1
    for i, existNum in enumerate(existNums):
        if existNum == 0:
            return [doubleNum, i+1]


if __name__ == '__main__':
    print(findErrorNums([6, 6, 3, 4, 1, 2]))