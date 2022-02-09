def permute(nums: [int]) -> [[int]]:
    def backtrack(index):
        if index == n:
            res.append(nums[:])
        for i in range(index, n):
            nums[index], nums[i] = nums[i], nums[index]
            backtrack(index + 1)
            nums[index], nums[i] = nums[i], nums[index]

    n = nums.__len__()
    res = []
    backtrack(0)
    return res


if __name__ == '__main__':
    print(permute([1,2,3]))
    print(permute([1,2,3,4,5,6,7]))
    print(permute([1]))
