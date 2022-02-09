def getMinDistance(nums: [int], target: int, start: int) -> int:
    res = 1000
    for i, num in enumerate(nums):
        if num == target:
            res = min(abs(start-i), res)
    return res


if __name__ == '__main__':
    print(getMinDistance(nums = [1,2,3,4,5], target = 5, start = 3))
    print(getMinDistance(nums = [1], target = 1, start = 0))
    print(getMinDistance(nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0))
