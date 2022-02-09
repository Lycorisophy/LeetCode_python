def nextGreaterElements(nums: [int]) -> [int]:
    n = nums.__len__()
    res = [-1] * n
    s = []
    for i in range(n*2-1):
        num = nums[i % n]
        while s and num > nums[s[-1]]:
            last = s.pop(-1)
            res[last] = num
        s.append(i % n)
    return res


if __name__ == '__main__':
    print(nextGreaterElements([1, 2, 1]))
    print(nextGreaterElements([1, 2, 3, 4]))
    print(nextGreaterElements([4, 3, 2, 1]))
