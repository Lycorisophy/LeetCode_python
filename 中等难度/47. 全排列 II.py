def permuteUnique(nums: [int]) -> [[int]]:
    def backtrack(index, tmp):
        if index == n:
            res.append(tmp.copy())
            return
        for i in range(n):
            if vis[i] or (i > 0 and nums[i] == nums[i - 1] and not vis[i - 1]):
                continue
            tmp.append(nums[i])
            vis[i] = True
            backtrack(index+1, tmp)
            vis[i] = False
            tmp.pop(index)

    nums.sort()
    n = nums.__len__()
    res = []
    vis = [False]*n
    backtrack(0, [])
    return res


if __name__ == '__main__':
    print(permuteUnique([1, 1, 2]))
    print(permuteUnique([1, 2, 3]))
    print(permuteUnique([1, 2, 3, 2, 4, 4]))
