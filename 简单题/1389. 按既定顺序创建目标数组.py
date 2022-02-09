def createTargetArray(nums: [int], index: [int]) -> [int]:
    target = []
    for num, i in zip(nums, index):
        target = target[:i] + [num] + target[i:]
    return target


if __name__ == '__main__':
    print(createTargetArray(nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1]))
    print(createTargetArray([1, 2, 3, 4, 0], index=[0, 1, 2, 3, 0]))
    print(createTargetArray(nums=[1], index=[0]))
