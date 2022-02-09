def subsets(nums: [int]) -> [[int]]:
    def combine(n: int, k: int) -> [[int]]:
        def backtrack(tmp, index):
            if tmp.__len__() == k:
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
    print(subsets([1, 2, 3]))
    print(subsets([0]))
    print(subsets([1, 2, 3, 4, 5]))
