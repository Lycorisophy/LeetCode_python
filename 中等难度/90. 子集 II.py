def subsetsWithDup(nums: [int]) -> [[int]]:
    def combine(n: int, k: int) -> [[int]]:
        def backtrack(tmp, index):
            if tmp.__len__() == k:
                tmp.sort()
                if tmp not in res:
                    res.append(tmp)
                return
            for i in range(index, n):
                backtrack(tmp + [nums[i]], i + 1)

        res = []
        backtrack([], 0)
        return res

    ans = [[], nums]
    m = nums.__len__()
    for i in range(1, m):
        ans += combine(m, i)
    return ans


if __name__ == '__main__':
    print(subsetsWithDup([4,4,4,1,4]))
    print(subsetsWithDup([0]))
    print(subsetsWithDup([1, 2, 3, 3, 3]))
